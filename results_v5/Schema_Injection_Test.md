# Schema Injection Test

## Injected Blueprint (Mistral)
```text
```
k1 = 0.1 * (x + y)
k2 = 0.1 * ((x + 0.05) + (y + k1/2))
k3 = 0.1 * ((x + 0.05) + (y + k2/2))
k4 = 0.1 * ((x + 0.1) + (y + k3))

y_new = y + (k1 + 2*k2 + 2*k3 + k4)/6
x_new = x + 0.1
```
```

## Student Execution (Qwen 0.5B)
```
k1 = 0.1 * (0.0 + 1.0) = 0.1
k2 = 0.1 * ((0.0 + 0.05) + (1.0 + 0.1/2)) = 0.11
k3 = 0.1 * ((0.0 + 0.05) + (1.0 + k1/2)) = 0.14
k4 = 0.1 * ((0.0 + 0.1) + (1.0 + k3)) = 0.17
y_new = y + (k1 + 2*k2 + 2*k3 + k4)/6 = 0.185
x_new = x + 0.1 = 0.1
```

## Audit
{
  "status": "FAILURE",
  "error_point": [
    {
      "step": "k2",
      "error": "Incorrect calculation. Correct formula for k2 should be: k2 = h * (f(x + h/2, y + k1/2)). Here, f(x + h/2, y + k1/2) = (0.0 + 0.05) + (1.0 + 0.1/2) = 1.15, so k2 = 0.1 * 1.15 = 0.115 (not 0.11)."
    },
    {
      "step": "k3",
      "error": "Incorrect calculation. Correct formula for k3 should be: k3 = h * (f(x + h/2, y + k2/2)). Here, f(x + h/2, y + k2/2) = (0.0 + 0.05) + (1.0 + 0.115/2) = 1.1075, so k3 = 0.1 * 1.1075 = 0.11075 (not 0.1105 or 0.14)."
    },
    {
      "step": "k4",
      "error": "Incorrect calculation. Correct formula for k4 should be: k4 = h * (f(x + h, y + k3)). Here, f(x + h, y + k3) = (0.1 + 0.11075) + (1.0 + 0.11075) = 1.3215, so k4 = 0.1 * 1.3215 = 0.13215 (not 0.12105 or 0.17)."
    },
    {
      "step": "y_new",
      "error": "Incorrect final calculation. Correct y_new should be: y_new = y + (k1 + 2*k2 + 2*k3 + k4)/6 = 1.0 + (0.1 + 2*0.115 + 2*0.11075 + 0.13215)/6 = 1.110342 (not 0.185)."
    }
  ],
  "score": 2
}