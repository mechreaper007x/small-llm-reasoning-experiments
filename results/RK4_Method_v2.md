# RK4_Method - Loop 2

## Code
```python
```python3
import numpy as np

def solve_ode(y0, x0, h, f):
    """
    Solve an ordinary differential equation (ODE) using the RK4 method.
    
    Parameters:
    - y0: Initial value of y
    - x0: Starting point for integration
    - h: Step size
    - f: Function representing the ODE
    
    Returns:
    - y: Solution at each step
    """
    k1 = f(y0, x0 + h)
    k2 = f(y0 + 0.5 * h, x0 + h + 0.5 * h * k1)
    k3 = f(y0 + 0.5 * h, x0 + 0.5 * h * k1 + 0.5 * h * k2)
    k4 = f(y0 + h, x0 + h + 0.5 * h * k1 + 0.5 * h * k2 + 0.5 * h * k3)
    
    return y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6

def rk4(y, x, h):
    """
    Compute the RK4 method for a given ODE.
    
    Parameters:
    - y: Current value of y
    - x: Starting point for integration
    - h: Step size
    
    Returns:
    - y: Solution at each step
    """
    k1 = f(y, x + h)
    k2 = f(y + 0.5 * h, x + 0.5 * h * k1)
    k3 = f(y + 0.5 * h, x + 0.5 * h * k1 + 0.5 * h * k2)
    k4 = f(y + h, x + h + 0.5 * h * k1 + 0.5 * h * k2 + 0.5 * h * k3)
    
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

def rk4_method(y0, x0, h, f):
    """
    Solve the ODE using the RK4 method.
    
    Parameters:
    - y0: Initial value of y
    - x0: Starting point for integration
    - h: Step size
    - f: Function representing the ODE
    
    Returns:
    - y: Solution at each step
    """
    y = np.array([y0])
    while True:
        y = rk4(y, x0, h)
        x0 = y[0]
        if abs(x0 - y[1]) < 1e-6:
            break
        h /= 2

# Example usage
y0 = 1.0
x0 = 0.0
h = 0.1
f = lambda y, x: y + x * y

rk4_method(y0, x0, h, f)
```
```

## Oracle Output
  File "C:\Users\SAVYAS~1\AppData\Local\Temp\tmpqkfdqgnc.py", line 1
    ```python3
    ^
SyntaxError: invalid syntax


## Student Ledger
```python
import numpy as np

def rk4(y, h):
    k1 = h * y[0]
    k2 = h * (y[0] + y[1]) / 2.0
    k3 = h * (y[1] + y[2]) / 2.0
    k4 = h * (y[2] + y[3]) / 2.0
    return y + (k1 + 2*k2 + 2*k3 + k4) / 6

def solve_ode(y, x):
    n = len(x)
    for i in range(n-1):
        y[i+1] = y[i]
        y[i+1] = rk4(y[i+1], x[i+1] - x[i])
    return y

y = [1.0] * 5
x = np.linspace(0, 2, 5)
h = 0.1
y = solve_ode(y, x)

print("Initial values:", y)
print("Intermediate steps:")
k1, k2, k3, k4 = rk4(y, h)
print("k1 =", k1, "k2 =", k2, "k3 =", k3, "k4 =", k4)
```