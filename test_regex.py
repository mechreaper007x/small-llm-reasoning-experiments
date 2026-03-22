import re
import json

raw = """```json
{
  "status": "FAILURE",
  "surgical_feedback": [
    {
      "step": "Step 1: ODE Definition",
      "issue": "The ODE was incorrectly rewritten. The given ODE is **already in the correct form** for the RK4 method: **f(x, y) = x + y**. The student incorrectly transformed it into a non-standard form (e.g., **dy/dx - y = x**) and then misapplied the RK4 coefficients. The correct form for RK4 is **y' = f(x, y)**, where **f(x, y) = x + y**.",
      "correction": "Use **f(x, y) = x + y** directly in the RK4 formula. The student also incorrectly assumed **k1 = 0.1** (should be **k1 = h * f(x_n, y_n) = 0.1 * (0 + 1) = 0.1** but then misapplied it)."
    }
  ],
  "survival_score": 2
}
```"""

match = re.search(r'(\{.*\})', raw, re.DOTALL)
if match:
    try:
        data = json.loads(match.group(1))
        print("SUCCESS")
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"FAILED JSON: {e}")
else:
    print("FAILED REGEX")
