# Loop 1

## Code
def rk4(y, x, h):
    k1 = f(x, y, h)
    k2 = f(x + 0.5 * h, y + 0.5 * k1, h)
    k3 = f(x + 0.5 * h, y + 0.5 * k2, h)
    k4 = f(x + h, y + k3, h)
    return [k1, k2, k3, k4]

def f(x, y, h):
    return x + y

y = 1
x = 0
h = 0.1
steps = 50
for i in range(steps):
    y = rk4(y, x, h)
    x += h

## Oracle
Traceback (most recent call last):
  File "C:\Users\SAVYAS~1\AppData\Local\Temp\tmp41m5db32.py", line 16, in <module>
    y = rk4(y, x, h)
        ^^^^^^^^^^^^
  File "C:\Users\SAVYAS~1\AppData\Local\Temp\tmp41m5db32.py", line 2, in rk4
    k1 = f(x, y, h)
         ^^^^^^^^^^
  File "C:\Users\SAVYAS~1\AppData\Local\Temp\tmp41m5db32.py", line 9, in f
    return x + y
           ~~^~~
TypeError: unsupported operand type(s) for +: 'float' and 'list'


## Ledger
```python
import numpy as np

def rk4(y, x, h):
    k1 = f(x, y, h)
    k2 = f(x + 0.5 * h, y + 0.5 * h * k1, h / 2)
    k3 = f(x + 0.5 * h, y + 0.5 * h * k2, h / 2)
    k4 = f(x + h, y + k3, h)
    return [k1, k2, k3, k4]

def f(x, y, h):
    return x + y

y = np.array([1])
x = 0
h = 0.1
for _ in range(5):  # Run the RK4 method for 5 steps
    y = rk4(y, x, h)
```