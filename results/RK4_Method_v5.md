# RK4_Method - Loop 5

## Code
```python
import numpy as np

def rk4(y, h):
    k1 = h * y[0]
    k2 = h * (y[0] + y[1]) / 2
    k3 = h * (y[1] + y[2]) / 2
    k4 = h * (y[2] + y[3]) / 2
    
    return [k1, k2, k3, k4]

x = np.linspace(0, 1, 100)
y = [rk4([1], i) for i in x]
print(y)

# Find y(0.2)
y_0_2 = rk4([1], 0.1)
print(f"y(0.2) = {y_0_2[0]}")
```

## Oracle Output
Traceback (most recent call last):
  File "C:\Users\SAVYAS~1\AppData\Local\Temp\tmpswm15jyx.py", line 12, in <module>
    y = [rk4([1], i) for i in x]
         ^^^^^^^^^^^
  File "C:\Users\SAVYAS~1\AppData\Local\Temp\tmpswm15jyx.py", line 5, in rk4
    k2 = h * (y[0] + y[1]) / 2
                     ~^^^
IndexError: list index out of range


## Student Ledger
### MATH LEDGER
1. **Initial Matrix**: [Values]
2. **Intermediate Steps**: 
   - `k1`: [x, y, z]
   - `k2`: [x + h/2, (y + 2*z)/h, (z + 2*y)/h]
   - `k3`: [x + h/3, (y + 3*z)/h + k2[1], (z + 3*y)/h + k2[2]]
   - `k4`: [x + h/6, (y + 4*z)/h + k2[3], (z + 4*y)/h + k2[4]]
3. **Final Answer**: [x, y, z]