import json
import re
import requests
import os
from dotenv import load_dotenv

# ── CONFIG ──────────────────────────────────────────────────────────────────
load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_URL = "https://api.mistral.ai/v1/chat/completions"
MISTRAL_MODEL = "open-mistral-7b" 

OLLAMA_URL = "http://localhost:11434/api/chat"
STUDENT_MODEL = "qwen2.5:0.5b"

RESULTS_DIR = "results_v5"
if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)

# ── CORE CALLS ───────────────────────────────────────────────────────────────
def call_student(system_prompt: str, user_message: str) -> str:
    payload = {
        "model": STUDENT_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_message},
        ],
        "stream": False,
        "options": {"temperature": 0.0, "num_predict": 512}
    }
    response = requests.post(OLLAMA_URL, json=payload, timeout=90)
    return response.json()["message"]["content"].strip()

def call_advisor(system_prompt: str, user_message: str) -> str:
    headers = {"Authorization": f"Bearer {MISTRAL_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": MISTRAL_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_message},
        ],
        "temperature": 0.0
    }
    response = requests.post(MISTRAL_URL, json=payload, headers=headers, timeout=60)
    return response.json()["choices"][0]["message"]["content"].strip()

# ── EXPERIMENT PHASES ──────────────────────────────────────────────────────

def generate_blueprint(ode: str, h: float) -> str:
    print("--- [Step 1] Advisor Generating Injected Blueprint ---")
    sys_prompt = """You are the SCHEMA INJECTOR.
The small model you are feeding is "Formula-Blind" and cannot process abstract functions like f(x,y).
Your job is to translate the RK4 method into a pure arithmetic blueprint for the specific ODE.
DO NOT use 'f'. Substitute the function directly into the RK4 steps.

Example for dy/dx = x * y, h=0.1:
k1 = 0.1 * (x * y)
k2 = 0.1 * ((x + 0.05) * (y + k1/2))
...
Output ONLY the text of the blueprint template, ready to be calculated."""
    user_prompt = f"Create the arithmetic blueprint for: {ode}, with step size h={h}. Use x and y as the variables."
    return call_advisor(sys_prompt, user_prompt)

def execute_blueprint(blueprint: str, x0: float, y0: float) -> str:
    print("--- [Step 2] Student Executing Injected Blueprint ---")
    sys_prompt = """You are an Arithmetic Calculator. You suffer from mathematical amnesia.
You must NOT write Python code.
You MUST strictly evaluate the INJECTED BLUEPRINT step-by-step using pure arithmetic.
Initial values are provided. Plug them in, do the arithmetic, and output the numerical result for each line.

Example Output format:
k1 = 0.1 * (0.0 + 1.0) = 0.1
k2 = 0.1 * ((0.0 + 0.05) + (1.0 + 0.1/2)) = 0.11
...
Final y_new = ..."""
    user_prompt = f"INITIAL VALUES: x = {x0}, y = {y0}\n\nINJECTED BLUEPRINT:\n{blueprint}\n\nCalculate the numerical value for each line."
    return call_student(sys_prompt, user_prompt)

def audit_execution(execution: str) -> dict:
    print("--- [Step 3] Advisor Auditing Execution ---")
    sys_prompt = """You are the ARITHMETIC AUDITOR.
Verify the student's arithmetic against the Absolute Truth for dy/dx = x+y, x=0, y=1, h=0.1:
k1=0.1, k2=0.11, k3=0.1105, k4=0.12105, y_new=1.110342.
Output ONLY JSON:
{
  "status": "SUCCESS" or "FAILURE",
  "error_point": "None or specific step where math failed",
  "score": 0-10
}"""
    raw = call_advisor(sys_prompt, execution)
    start = raw.find('{')
    end = raw.rfind('}')
    if start != -1 and end != -1:
        return json.loads(raw[start:end+1], strict=False)
    return {"status": "FAILURE", "error_point": "Parse Error", "score": 0}

def run_injection_test():
    print(f"\n=== [SCHEMA INJECTION LOOP: RK4] ===")
    ode = "dy/dx = x + y"
    h = 0.1
    x0, y0 = 0.0, 1.0

    # 1. Blueprint
    blueprint = generate_blueprint(ode, h)
    print(f"\n[Blueprint Generated]\n{blueprint}\n")

    # 2. Execution
    execution = execute_blueprint(blueprint, x0, y0)
    print(f"\n[Student Execution]\n{execution}\n")

    # 3. Audit
    audit = audit_execution(execution)
    print(f"\n[Audit Result]: {audit.get('status')} (Score: {audit.get('score')}/10)")
    if audit.get('status') == "FAILURE":
        print(f"Error Point: {audit.get('error_point')}")

    with open(f"{RESULTS_DIR}/Schema_Injection_Test.md", "w") as f:
        f.write(f"# Schema Injection Test\n\n## Injected Blueprint (Mistral)\n```text\n{blueprint}\n```\n\n## Student Execution (Qwen 0.5B)\n{execution}\n\n## Audit\n{json.dumps(audit, indent=2)}")

if __name__ == "__main__":
    run_injection_test()
