import json
import re
import subprocess
import sys
import tempfile
import requests
import os
from datetime import datetime
from typing import Generator
from dotenv import load_dotenv

# ── CONFIG ──────────────────────────────────────────────────────────────────
load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_URL = "https://api.mistral.ai/v1/chat/completions"
MISTRAL_MODEL = "open-mistral-7b" 

OLLAMA_URL = "http://localhost:11434/api/chat"
STUDENT_MODEL = "qwen2.5:0.5b"

MAX_LOOPS = 6 
RESULTS_DIR = "results_v3"

if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)

# ── CORE CALLS ───────────────────────────────────────────────────────────────
def call_student(system_prompt: str, user_message: str, temperature: float) -> str:
    payload = {
        "model": STUDENT_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_message},
        ],
        "stream": False,
        "options": {"temperature": temperature, "num_predict": 1024}
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=90)
        return response.json()["message"]["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

def call_advisor(system_prompt: str, user_message: str, temperature: float) -> str:
    headers = {"Authorization": f"Bearer {MISTRAL_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": MISTRAL_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_message},
        ],
        "temperature": temperature
    }
    try:
        response = requests.post(MISTRAL_URL, json=payload, headers=headers, timeout=60)
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# ── STEP 1: TRUTH ANCHORING (UNMODIFIED) ───────────────────────────────────
def advisor_generate_truth_anchor(query: str) -> str:
    system = """You are the ORACLE ARCHITECT.
Write a Python script using numpy/scipy/sympy to find the ABSOLUTE MATHEMATICAL TRUTH.
Output ONLY the code block."""
    user = f"Problem: {query}"
    resp = call_advisor(system, user, temperature=0.0)
    match = re.search(r"```python\n(.*?)\n```", resp, re.DOTALL)
    return match.group(1).strip() if match else resp.strip()

def execute_code(code: str) -> str:
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
        f.write(code); temp_path = f.name
    try:
        exec_res = subprocess.run([sys.executable, temp_path], capture_output=True, text=True, timeout=15)
        return (exec_res.stdout + exec_res.stderr).strip()
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

# ── STEP 2: PURE MATHEMATICAL DERIVATION (STUDENT) ──────────────────────────
def student_derive_math(query: str, absolute_truth: str, history: list) -> str:
    memory_block = ""
    for attempt in history[-1:]:
        memory_block += f"\nLAST ATTEMPT MATHEMATICAL ERROR: {attempt['surgical_feedback']}\n"

    system = """You are a Mathematics Professor.
Solve the problem using a step-by-step mathematical derivation.
MANDATES:
1. Do NOT write any Python code.
2. Show every calculation step clearly.
3. Aim to reach the ABSOLUTE TRUTH provided.
4. If you made a previous error, fix the specific formula or step mentioned in the feedback.
Format your response with numbered steps."""
    
    user = f"Problem: {query}\n\nABSOLUTE TRUTH (Goal):\n{absolute_truth}\n{memory_block}\n\nCOMMAND: Provide the Step-by-Step Mathematical Derivation."
    return call_student(system, user, temperature=0.2)

# ── STEP 3: MATHEMATICAL SURGICAL AUDIT (ADVISOR) ───────────────────────────
def advisor_math_audit(derivation: str, absolute_truth: str) -> dict:
    system = """You are the MATHEMATICAL AUDITOR.
Compare the Student's step-by-step derivation against the Absolute Truth.
Identify exactly which STEP or FORMULA is wrong.
MANDATE:
1. Be extremely specific (e.g., "Step 3: You used the Sample SD formula instead of Population").
2. Check if the final result matches the Absolute Truth.
Output ONLY JSON:
{
  "status": "SUCCESS" or "FAILURE",
  "surgical_feedback": "In Step X, you used formula Y, but for this problem, Z is required because...",
  "survival_score": 0-10
}"""
    user = f"STUDENT DERIVATION:\n{derivation}\n\nABSOLUTE TRUTH:\n{absolute_truth}"
    raw = call_advisor(system, user, temperature=0.0)
    print(f"DEBUG: Raw Advisor Audit Response:\n{raw}")
    
    # Robust JSON extraction: Find the first '{' and the last '}'
    start_idx = raw.find('{')
    end_idx = raw.rfind('}')
    
    if start_idx != -1 and end_idx != -1:
        json_str = raw[start_idx:end_idx+1]
        try:
            return json.loads(json_str, strict=False)
        except Exception as e:
            print(f"DEBUG: JSON Load Error: {e}")
            return {"status": "FAILURE", "surgical_feedback": "Parse Error: Invalid JSON structure", "survival_score": 0}
    else:
        return {"status": "FAILURE", "surgical_feedback": "Parse Error: No JSON found", "survival_score": 0}

# ── EXECUTION LOOP ───────────────────────────────────────────────────────────
def run_math_loop(query: str, test_name: str):
    print(f"\n=== [PURE MATH LOOP: {test_name}] ===")
    
    # 1. TRUTH ANCHORING
    print("--- [Step 1] Advisor Finding Absolute Truth ---")
    truth_script = advisor_generate_truth_anchor(query)
    absolute_truth = execute_code(truth_script)
    print(f"Absolute Truth found:\n{absolute_truth}")
    
    history_log, loop = [], 0
    while loop < MAX_LOOPS:
        loop += 1
        print(f"\n--- [Loop {loop}] Student Deriving Math ---")
        
        # 2. MATH DERIVATION
        derivation = student_derive_math(query, absolute_truth, history_log)
        
        # 3. SURGICAL AUDIT
        audit = advisor_math_audit(derivation, absolute_truth)
        score = int(audit.get("survival_score", 0))
        feedback_raw = audit.get("surgical_feedback", "N/A")
        
        # Convert list feedback to a bulleted string for the student
        if isinstance(feedback_raw, list):
            feedback = "\n".join([f"- {item}" for item in feedback_raw])
        else:
            feedback = str(feedback_raw)
            
        status = audit.get("status", "FAILURE")
        
        print(f"  Result: {status} (Score {score}/10)")
        if status == "FAILURE":
            print(f"  Feedback: {feedback}")

        # Save to results
        filename = f"{RESULTS_DIR}/{test_name}_v{loop}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Loop {loop}\n\n## Absolute Truth\n{absolute_truth}\n\n## Student Math Derivation\n{derivation}\n\n## Surgical Audit\n{json.dumps(audit, indent=2)}")

        if score >= 9:
            print(f"[✓] SUCCESS: Student reached logical parity through pure math!")
            return

        history_log.append({
            "loop": loop,
            "derivation": derivation,
            "surgical_feedback": feedback
        })

    print(f"[!] FAILURE: Logic gap persists in pure mathematical reasoning.")

if __name__ == "__main__":
    # We re-run the RK4 test because this is where code generation failed previously
    query = "Solve the ODE dy/dx = x + y with y(0) = 1 using the RK4 method. Find y(0.1) using step size h = 0.1. Show every step of the calculation for k1, k2, k3, k4."
    run_math_loop(query, "RK4_Math_Loop")
