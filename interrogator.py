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
SURVIVAL_THRESHOLD = 9 
RESULTS_DIR = "results"

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

# ── MEMORY BRIDGE PROMPTS ───────────────────────────────────────────────────
def student_write_code_with_bridge(query: str, history: list) -> str:
    memory_block = ""
    for attempt in history[-2:]:
        # Explicitly highlighting the 'Better Code' from the Ledger
        better_code = attempt.get('better_code', 'No code found in ledger.')
        memory_block += f"""
--- MEMORY: ATTEMPT {attempt['loop']} ---
FAILED EXECUTION CODE:
{attempt['code']}

ORACLE ERROR:
{attempt['ground_truth']}

ADVISOR FEEDBACK:
{attempt['feedback']}

YOU WROTE THIS CORRECTED CODE IN YOUR PREVIOUS LEDGER:
{better_code}
-------------------------------------------
"""
    
    system = """You are a Python Programmer.
You must solve the B.Tech Math problem.
CRITICAL: The code in your MEMORY's 'PREVIOUS LEDGER' section is closer to being correct. 
START FROM THAT CODE. Do NOT repeat the mistakes of the 'FAILED EXECUTION CODE'.

To fix the logic, you MUST first think step-by-step in a <thought> block.
1. Write down the exact mathematical formula needed.
2. Identify what went wrong in the previous execution.
3. Plan the Python code structure.

After thinking, output the corrected code.

FORMAT:
<thought>
[Your step-by-step mathematical reasoning]
</thought>
```python
[Your Python code]
```"""
    
    user = f"Problem: {query}\n\nYOUR EPISODIC MEMORY:\n{memory_block}\n\nCOMMAND: Think step-by-step, then provide the corrected code."
    return call_student(system, user, temperature=0.2)

def student_write_ledger(query: str, ground_truth: str) -> str:
    system = """You are a Mathematics Clerk. 
Explain the solution based ONLY on the Python output provided.
IMPORTANT: In your ledger, include a ```python code block``` showing the corrected script that should have been used.
Use the values exactly as they appear in the Oracle output."""
    user = f"Problem: {query}\n\nPYTHON GROUND TRUTH:\n{ground_truth}"
    return call_student(system, user, temperature=0.2)

def advisor_audit(ledger: str, ground_truth: str) -> dict:
    system = """You are the BRUTAL AUDITOR. 
Compare the Student's Ledger against the PYTHON GROUND TRUTH.
Output ONLY JSON:
{
  "survival_score": 0-10,
  "remediation": "Concise list of discrepancies",
  "hallucination_detected": true/false
}"""
    user = f"STUDENT LEDGER:\n{ledger}\n\nPYTHON GROUND TRUTH:\n{ground_truth}"
    raw = call_advisor(system, user, temperature=0.0)
    match = re.search(r'\{.*\}', raw, re.DOTALL)
    try:
        data = json.loads(match.group(0)) if match else {}
        return data
    except:
        return {"survival_score": 0, "remediation": "Invalid Advisor JSON"}

# ── EXECUTION LOOP ───────────────────────────────────────────────────────────
def run_bridged_test(query: str, test_name: str):
    print(f"\n=== [BRIDGED TEST: {test_name}] ===")
    history_log, loop = [], 0
    
    while loop < MAX_LOOPS:
        loop += 1
        print(f"\n--- [Loop {loop}] Student Generating Code (Memory + Ledger Bridge) ---")
        
        # 1. Code Generation with Bridge
        code_resp = student_write_code_with_bridge(query, history_log)
        code_match = re.search(r"```python\n(.*?)\n```", code_resp, re.DOTALL)
        code = code_match.group(1).strip() if code_match else code_resp.strip()
        
        # 2. Execution (The Oracle)
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
            f.write(code); temp_path = f.name
        exec_res = subprocess.run([sys.executable, temp_path], capture_output=True, text=True, timeout=10)
        ground_truth = exec_res.stdout + exec_res.stderr
        
        # 3. Ledger Generation (Mandatory code block inside)
        ledger = student_write_ledger(query, ground_truth)
        
        # 4. Save to Audit Trail
        filename = f"{RESULTS_DIR}/{test_name}_v{loop}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Loop {loop}\n\n## Submitted Code\n```python\n{code}\n```\n\n## Oracle Result\n{ground_truth}\n\n## Student Ledger\n{ledger}")

        # 5. Truth Audit
        audit_res = advisor_audit(ledger, ground_truth)
        score = int(audit_res.get("survival_score", 0))
        feedback = audit_res.get("remediation", "Fix discrepancies.")
        
        print(f"  Result: Score {score}/10")
        
        # 6. EXTRACT BETTER CODE FROM LEDGER FOR NEXT LOOP
        better_code_match = re.search(r"```python\n(.*?)\n```", ledger, re.DOTALL)
        better_code = better_code_match.group(1).strip() if better_code_match else code
        
        history_log.append({
            "loop": loop,
            "code": code,
            "ground_truth": ground_truth,
            "feedback": feedback,
            "better_code": better_code
        })

        if score >= SURVIVAL_THRESHOLD:
            print(f"[✓] SUCCESS: Ledger Bridge synchronized the model's logic!")
            return

    print(f"[!] FAILURE: 0.5B model remains bifurcated.")

if __name__ == "__main__":
    query = "Solve the ODE dy/dx = x + y with y(0) = 1 using the RK4 method. Find y(0.2) using step size h = 0.1. You MUST print k1, k2, k3, k4 for each step."
    run_bridged_test(query, "RK4_Bridged_Test")
