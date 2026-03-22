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

RESULTS_DIR = "results_v4"
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
        "options": {"temperature": 0.0, "num_predict": 256} # Low temp, short response
    }
    response = requests.post(OLLAMA_URL, json=payload, timeout=60)
    return response.json()["message"]["content"].strip()

def call_advisor_json(system_prompt: str, user_message: str) -> dict:
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
    raw = response.json()["choices"][0]["message"]["content"].strip()
    
    start_idx = raw.find('{')
    end_idx = raw.rfind('}')
    if start_idx != -1 and end_idx != -1:
        return json.loads(raw[start_idx:end_idx+1], strict=False)
    return {"error": "Parse Error"}

# ── ATOMIC FACTORING STEPS ─────────────────────────────────────────────────

def calculate_step(prompt: str, name: str):
    print(f"  > Calculating {name}...")
    system = "You are a Mathematical Calculator. Provide ONLY the numerical result and the single formula line used. No conversational text."
    return call_student(system, prompt)

def run_atomic_rk4(query: str):
    print(f"\n=== [ATOMIC LOGIC LOOP: RK4] ===")
    
    # Initial State
    x, y, h = 0.0, 1.0, 0.1
    f_str = "f(x, y) = x + y"
    
    # 1. Calculate K1
    k1_prompt = f"Problem: {f_str}, x={x}, y={y}, h={h}. Calculate k1 = h * f(x, y)."
    k1_res = calculate_step(k1_prompt, "k1")
    
    # 2. Calculate K2
    k2_prompt = f"Problem: {f_str}, x={x}, y={y}, h={h}, previous k1={k1_res}. Calculate k2 = h * f(x + h/2, y + k1/2)."
    k2_res = calculate_step(k2_prompt, "k2")
    
    # 3. Calculate K3
    k3_prompt = f"Problem: {f_str}, x={x}, y={y}, h={h}, previous k2={k2_res}. Calculate k3 = h * f(x + h/2, y + k2/2)."
    k3_res = calculate_step(k3_prompt, "k3")
    
    # 4. Calculate K4
    k4_prompt = f"Problem: {f_str}, x={x}, y={y}, h={h}, previous k3={k3_res}. Calculate k4 = h * f(x + h, y + k3)."
    k4_res = calculate_step(k4_prompt, "k4")
    
    # 5. Final Sum
    sum_prompt = f"Initial y={y}, k1={k1_res}, k2={k2_res}, k3={k3_res}, k4={k4_res}. Calculate y_next = y + (1/6)*(k1 + 2*k2 + 2*k3 + k4)."
    final_res = calculate_step(sum_prompt, "Final y(0.1)")
    
    full_derivation = f"k1: {k1_res}\nk2: {k2_res}\nk3: {k3_res}\nk4: {k4_res}\nFinal Result: {final_res}"
    print(f"\nFull Atomic Derivation:\n{full_derivation}")
    
    # 6. Advisor Audit
    print("\n--- [Step 6] Advisor Auditing Atomic Chain ---")
    audit_sys = """You are the ATOMIC MATH AUDITOR.
Verify the 4-step RK4 calculation. The Absolute Truth for dy/dx = x+y, y(0)=1, h=0.1 is:
k1=0.1, k2=0.11, k3=0.1105, k4=0.12105, y(0.1)=1.110342.
Identify which Atomic Step failed first.
Output ONLY JSON:
{
  "failed_step": "k1/k2/k3/k4/sum",
  "error_description": "Specific math error",
  "survival_score": 0-10
}"""
    audit = call_advisor_json(audit_sys, full_derivation)
    print(f"Audit Result: Score {audit.get('survival_score')}/10")
    print(f"Error: {audit.get('error_description')}")

    # Save Results
    with open(f"{RESULTS_DIR}/RK4_Atomic_Test.md", "w") as f:
        f.write(f"# Atomic RK4 Test\n\n## Student Steps\n{full_derivation}\n\n## Advisor Audit\n{json.dumps(audit, indent=2)}")

if __name__ == "__main__":
    run_atomic_rk4("Solve dy/dx = x + y, y(0)=1, h=0.1 using RK4.")
