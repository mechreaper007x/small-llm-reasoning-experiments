# Loop 3

## Submitted Code
```python
import numpy as np

def f(x, y):
    return x + y

def rk4(f, x0, h, y0):
    k1 = h * f(x0, y0)
    k2 = h * f(x0 + 0.5*h, y0 + 0.5*k1)
    k3 = h * f(x0 + 0.5*h, y0 + 0.5*k2)
    k4 = h * f(x0 + h, y0 + k3)

    return x0 + (k1 + 2*k2 + 2*k3 + k4) / 6

x0 = 0
y0 = 1
h = 0.1
y = rk4(f, x0, h, y0)
print(y)
```

## Oracle Result
0.11034166666666667


## Student Ledger
```python
import numpy as np

def f(x, y):
    return x + y

def rk4(f, x0, h, y0):
    k1 = h * f(x0, y0)
    k2 = h * f(x0 + 0.5 * h, y0 + 0.5 * k1)
    k3 = h * f(x0 + 0.5 * h, y0 + 0.5 * k2)
    k4 = h * f(x0 + h, y0 + k3)

    return x0 + (k1 + 2*k2 + 2*k3 + k4) / 6

x0 = 0
y0 = 1
h = 0.1
y = rk4(f, x0, h, y0)
print(y)
```