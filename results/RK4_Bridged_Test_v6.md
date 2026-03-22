# Loop 6

## Submitted Code
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

## Oracle Result
0.11034166666666667


## Student Ledger
```python
import numpy as np

def rk4(y, h):
    x = y[0]
    y = [y[0]]
    for i in range(len(y)):
        k1 = h * (x + y[i])
        k2 = h * (x + y[i] + 0.5 * k1)
        k3 = h * (x + y[i] + 0.5 * k2)
        k4 = h * (x + y[i] + k3)
        y.append(k4)
    return y

y = np.array([1])
h = 0.1
k1, k2, k3, k4 = rk4(y, h)

print(f"k1: {k1}")
print(f"k2: {k2}")
print(f"k3: {k3}")
print(f"k4: {k4}")

y[0] = y[0] + 0.2
```