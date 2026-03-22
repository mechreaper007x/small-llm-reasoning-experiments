# RK4_Method - Loop 4

## Code
```python
import numpy as np

def solve_ode(y, x, h):
    k1 = y[0] + x * y[1]
    k2 = y[0] + 2 * x * y[1] / 3
    k3 = y[0] + 3 * x * y[1] / 5
    k4 = y[0] + 4 * x * y[1] / 7
    return np.array([k1, k2, k3, k4])

def rk4(y, x, h):
    n = int((x - y) / h)
    k1 = solve_ode(y, x, h / 2)
    k2 = solve_ode(y + (h / 2), x, h / 2)
    k3 = solve_ode(y + (h / 2), x + h / 4, h / 2)
    k4 = solve_ode(y + (h / 2), x + h, h / 2)
    return np.array([k1, k2, k3, k4])

y0 = 1
x = 0.5
h = 0.1
k1, k2, k3, k4 = rk4(y0, x, h)

print("Initial Matrix:", y0)
print("Step Size:", h)
print("Final Values:")
print(rk4(y0, x, h))
```

## Oracle Output
Traceback (most recent call last):
  File "C:\Users\SAVYAS~1\AppData\Local\Temp\tmpqh61uh9w.py", line 21, in <module>
    k1, k2, k3, k4 = rk4(y0, x, h)
                     ^^^^^^^^^^^^^
  File "C:\Users\SAVYAS~1\AppData\Local\Temp\tmpqh61uh9w.py", line 12, in rk4
    k1 = solve_ode(y, x, h / 2)
         ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\SAVYAS~1\AppData\Local\Temp\tmpqh61uh9w.py", line 4, in solve_ode
    k1 = y[0] + x * y[1]
         ~^^^
TypeError: 'int' object is not subscriptable


## Student Ledger
### MATH LEDGER
1. **Initial Matrix**: [Values]
2. **Intermediate Steps**: [Steps from Python]
3. **Final Answer**: [x, y, z] = (0.5, 1.5, 1.75)