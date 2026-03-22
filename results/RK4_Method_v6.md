# RK4_Method - Loop 6

## Code
```python
import numpy as np

def rk4_step(func, x0, h, y0):
    k1 = func(x0 + h/2, y0)
    k2 = func(x0 + h/2, y0 + (h/2) * k1)
    k3 = func(x0 + h/2, y0 + (h/2) * k2)
    k4 = func(x0 + h, y0 + (h/2) * k3)

    return [x0 + h/6 * (k1 + 2*k2 + 2*k3 + k4), y0 + h/6 * (k1 + 2*k2 + 2*k3 + k4)]

def dy_dx(x, y):
    return x + y

# Initial conditions
x0 = 0
y0 = 1

# Step size
h = 0.1

# Solve the ODE using RK4 method
solution = rk4_step(dy_dx, x0, h, y0)

print(solution)
```

## Oracle Output
[0.11034177083333334, 1.1103417708333334]


## Student Ledger
### MATH LEDGER
1. **Initial Matrix**: [Values]
2. **Intermediate Steps**: [Steps from Python]
3. **Final Answer**: [k1, k2, k3, k4]