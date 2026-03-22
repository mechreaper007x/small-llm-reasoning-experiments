# Loop 5

## Submitted Code
```python
def f(x, y):
    return x + y
```

## Oracle Result


## Student Ledger
```python
import numpy as np

def f(x, y):
    return x + y

def rk4(f, x0, y0, h, n):
    k1 = h * f(x0, y0)
    k2 = h * f(x0 + 0.5*h, y0 + 0.5*k1)
    k3 = h * f(x0 + 0.5*h, y0 + 0.5*k2)
    k4 = h * f(x0 + h, y0 + k3)

    return x0 + (k1 + 2*k2 + 2*k3 + k4) / 6

x0, y0 = 0, 1
h = 0.1
n = int((np.log(5/h)) / np.log(2))
y_n = rk4(f, x0, y0, h, n)

print(y_n)
```