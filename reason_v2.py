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
RESULTS_DIR = "results_v2"

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

# ── IMPROVISATION 1: SYMBOLIC TRUTH ANCHORING ────────────────────────────────
def advisor_generate_truth_anchor(query: str) -> str:
    system = """You are the ORACLE ARCHITECT.
Your job is to write a Python script that calculates the ABSOLUTE MATHEMATICAL TRUTH for the given problem.
MANDATE:
1. Use robust libraries: numpy, scipy, or sympy.
2. If the problem is a standard calculation (like Mean/SD), use the standard library function (e.g., np.std).
3. Print the final answer clearly using simple, bug-free print statements. Avoid complex inline f-string ternary operations.
4. Output ONLY the python code block."""
    
    user = f"Problem: {query}\n\nWrite the verification script."
    resp = call_advisor(system, user, temperature=0.0)
    match = re.search(r"```python\n(.*?)\n```", resp, re.DOTALL)
    return match.group(1).strip() if match else resp.strip()

def execute_code(code: str) -> str:
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
        f.write(code); temp_path = f.name
    try:
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        exec_res = subprocess.run([sys.executable, temp_path], capture_output=True, text=True, timeout=15, env=env)
        return (exec_res.stdout + exec_res.stderr).strip()
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

# ── IMPROVISATION 2: STRATEGY-FIRST REASONING ────────────────────────────────
def student_generate_strategy(query: str, absolute_truth: str) -> str:
    system = """You are a Mathematical Strategist.
Given a problem and its Absolute Truth result, explain the mathematical strategy to reach that truth.
DO NOT write code. Focus on:
1. Identifying the correct formulas.
2. Planning the logical steps.
3. Aligning with the Absolute Truth provided."""
    
    user = f"Problem: {query}\n\nABSOLUTE TRUTH (Reference):\n{absolute_truth}\n\nCOMMAND: Provide the Mathematical Strategy."
    return call_student(system, user, temperature=0.2)

# ── IMPROVISATION 4: LIBRARY PRIORITY ───────────────────────────────────────
def student_generate_code_v2(query: str, strategy: str, absolute_truth: str, history: list) -> str:
    memory_block = ""
    for attempt in history[-1:]: # Only last attempt for surgical focus
        memory_block += f"\nLAST ATTEMPT FEEDBACK: {attempt['surgical_feedback']}\n"

    system = """You are an Expert Python Programmer.
Write a script to solve the problem.
MANDATES:
1. Follow the provided MATHEMATICAL STRATEGY.
2. Aim for the ABSOLUTE TRUTH result.
3. FORBIDDEN: Manual loops for standard mathematical derivations (e.g., don't write `sum(x)/len(x)` if `np.mean(x)` exists).
4. PRIORITY: Use numpy, scipy, or sympy.
5. Provide ONLY the code block."""
    
    user = f"Problem: {query}\n\nSTRATEGY:\n{strategy}\n\nABSOLUTE TRUTH:\n{absolute_truth}\n{memory_block}\n\nCOMMAND: Generate Python Code."
    resp = call_student(system, user, temperature=0.1)
    match = re.search(r"```python\n(.*?)\n```", resp, re.DOTALL)
    return match.group(1).strip() if match else resp.strip()

# ── IMPROVISATION 3: SURGICAL FEEDBACK ─────────────────────────────────────
def advisor_surgical_audit(code: str, output: str, absolute_truth: str) -> dict:
    system = """You are the SURGICAL AUDITOR.
Compare the Student's Code and Output against the Absolute Truth.
If it fails:
1. Identify the EXACT LINE of code that is wrong.
2. Provide the MATHEMATICAL CORRECTION for that line.
Output ONLY JSON:
{
  "status": "SUCCESS" or "FAILURE",
  "surgical_feedback": "Line X: Change Y to Z because...",
  "survival_score": 0-10
}"""
    user = f"STUDENT CODE:\n{code}\n\nSTUDENT OUTPUT:\n{output}\n\nABSOLUTE TRUTH:\n{absolute_truth}"
    raw = call_advisor(system, user, temperature=0.0)
    match = re.search(r'\{.*\}', raw, re.DOTALL)
    try:
        return json.loads(match.group(0)) if match else {"status": "FAILURE", "surgical_feedback": "Invalid JSON", "survival_score": 0}
    except:
        return {"status": "FAILURE", "surgical_feedback": "Parse Error", "survival_score": 0}

# ── EXECUTION LOOP ───────────────────────────────────────────────────────────
def run_scaffolded_test(query: str, test_name: str):
    print(f"\n=== [SCAFFOLDED TEST: {test_name}] ===")
    
    # 1. TRUTH ANCHORING
    print("--- [Step 1] Advisor Generating Truth Anchor ---")
    truth_script = advisor_generate_truth_anchor(query)
    absolute_truth = execute_code(truth_script)
    print(f"Absolute Truth found:\n{absolute_truth}")
    
    # 2. STRATEGY
    print("\n--- [Step 2] Student Generating Strategy ---")
    strategy = student_generate_strategy(query, absolute_truth)
    print(f"Strategy:\n{strategy[:200]}...")
    
    history_log, loop = [], 0
    while loop < MAX_LOOPS:
        loop += 1
        print(f"\n--- [Loop {loop}] Student Generating Code ---")
        
        # 3. CODE GENERATION
        code = student_generate_code_v2(query, strategy, absolute_truth, history_log)
        
        # 4. EXECUTION
        output = execute_code(code)
        
        # 5. SURGICAL AUDIT
        audit = advisor_surgical_audit(code, output, absolute_truth)
        score = int(audit.get("survival_score", 0))
        feedback = audit.get("surgical_feedback", "N/A")
        status = audit.get("status", "FAILURE")
        
        print(f"  Result: {status} (Score {score}/10)")
        if status == "FAILURE":
            print(f"  Feedback: {feedback}")

        # Save to results
        filename = f"{RESULTS_DIR}/{test_name}_v{loop}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Loop {loop}\n\n## Absolute Truth\n{absolute_truth}\n\n## Strategy\n{strategy}\n\n## Submitted Code\n```python\n{code}\n```\n\n## Output\n{output}\n\n## Surgical Audit\n{json.dumps(audit, indent=2)}")

        if score >= 9:
            print(f"[✓] SUCCESS: Model logic anchored to symbolic truth!")
            return

        history_log.append({
            "loop": loop,
            "code": code,
            "output": output,
            "surgical_feedback": feedback
        })

    print(f"[!] FAILURE: Scaffold could not bridge the logic gap.")

if __name__ == "__main__":
    query = "Find a root of f(x) = x**3 - x - 2 using the Newton-Raphson method. Start with initial guess x0 = 1.5. Perform exactly 3 iterations. Show the values of x_n, f(x_n), f'(x_n), and x_{n+1} at each step."
    run_scaffolded_test(query, "Newton_Scaffold_Test")
