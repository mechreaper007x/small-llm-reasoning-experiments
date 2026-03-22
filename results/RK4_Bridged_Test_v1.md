# Loop 1

## Submitted Code
```python
import numpy as np

def f(x, y):
    return x + y

h = 0.1
x = 0
y = 1
t = 0

while t < 0.2:
    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h, y + k3)

    x_new = x + t * (h/2)  # New value of x
    y_new = y + t * (k1 + 2*k2 + 2*k3 + k4)/6

    x, y = x_new, y_new
    t += h

print("y(0.2) =", y)
```

## Oracle Result
y(0.2) = 1.0110341666666667


## Student Ledger
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