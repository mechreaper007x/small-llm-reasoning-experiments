import json
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:0.5b"

def ask(question: str):
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": question}],
        "stream": False,
        "options": {"temperature": 0.0}
    }
    try:
        resp = requests.post(OLLAMA_URL, json=payload).json()
        return resp["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"

def run_knowledge_map():
    queries = {
        "Math (Numerical)": "What is the formula for the fourth-order Runge-Kutta method (RK4)? List k1, k2, k3, k4.",
        "Math (Linear)": "Explain Gauss-Seidel iteration and its convergence criteria.",
        "Physics (Thermo)": "State the Second Law of Thermodynamics in terms of entropy and heat engines.",
        "Engineering (Circuits)": "Define Kirchhoff's Voltage Law (KVL) and its relation to energy conservation.",
        "Programming (API)": "Write a Python snippet using scipy.integrate.solve_ivp to solve dy/dx = y.",
        "Obscure Concept": "What is the 'No-Hair Theorem' in black hole physics?",
        "Schema Limits": "Who is the current Prime Minister of India? (Checking training data cutoff)"
    }

    print(f"=== MAPPING 0.5B KNOWLEDGE BASE ===\n")
    results = {}
    for domain, q in queries.items():
        print(f"[*] Probing {domain}...")
        answer = ask(q)
        results[domain] = {"question": q, "answer": answer}
        
        # Print a snippet of the answer
        snippet = answer[:150].replace('\n', ' ')
        print(f"    > Response: {snippet}...\n")

    with open("knowledge_map_results.md", "w", encoding="utf-8") as f:
        f.write("# 0.5B Knowledge Base Mapping\n\n")
        for domain, data in results.items():
            f.write(f"## {domain}\n**Q**: {data['question']}\n\n**A**:\n{data['answer']}\n\n---\n")

if __name__ == "__main__":
    run_knowledge_map()
