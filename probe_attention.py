import json
import requests
import time

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:0.5b"

def probe_call(user_message: str):
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": user_message}],
        "stream": False,
        "options": {"temperature": 0.0}
    }
    start = time.time()
    resp = requests.post(OLLAMA_URL, json=payload).json()
    duration = time.time() - start
    return resp["message"]["content"].strip(), duration

def run_attention_probe():
    print(f"=== PROBING ATTENTION HEADS (BEHAVIORAL) ===")
    
    truth_value = "4.2708"
    
    # PROBE 1: Zero Noise (Baseline)
    print("\n[Probe 1] Baseline (Zero Noise)...")
    p1_msg = f"The standard deviation is {truth_value}. What is the standard deviation? Answer only with the number."
    res1, d1 = probe_call(p1_msg)
    print(f"  > Model Output: {res1} (Time: {d1:.2f}s)")

    # PROBE 2: Semantic Noise (Distraction)
    print("\n[Probe 2] Semantic Noise (Distraction)...")
    noise = "Bananas are yellow. The sky is blue. Computers process bits. " * 50
    p2_msg = f"{noise} The standard deviation is {truth_value}. {noise} What is the standard deviation? Answer only with the number."
    res2, d2 = probe_call(p2_msg)
    print(f"  > Model Output: {res2} (Time: {d2:.2f}s)")

    # PROBE 3: Attention Sink (Repetitive Noise)
    print("\n[Probe 3] Attention Sink (Repetition)...")
    sink = "the the the the the the the " * 100
    p3_msg = f"{sink} The standard deviation is {truth_value}. {sink} What is the standard deviation? Answer only with the number."
    res3, d3 = probe_call(p3_msg)
    print(f"  > Model Output: {res3} (Time: {d3:.2f}s)")

    print("\n=== ANALYSIS ===")
    if res1 == res2 == res3 == truth_value:
        print("RESULT: Attention Heads are stable. Hallucinations are NOT triggered by context length.")
    else:
        print("RESULT: ATTENTION COLLAPSE DETECTED.")
        if res2 != truth_value: print(f" - Distracted by Semantic Noise: {res2}")
        if res3 != truth_value: print(f" - Lost in Attention Sink: {res3}")

if __name__ == "__main__":
    run_attention_probe()
