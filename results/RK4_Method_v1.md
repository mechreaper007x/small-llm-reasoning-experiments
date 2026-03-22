# RK4_Method - Loop 1

## Code
```python
import numpy as np

def rk4(y, x, h):
    """
    Solve the ODE dy/dx = f(x, y) with initial condition y(x0) = y0 using the RK4 method.
    
    Parameters:
    - y: Initial value of y
    - x: Current value of x
    - h: Step size
    
    Returns:
    - y: Value of y after each step
    """
    k1 = f(y, x, h)
    k2 = f(y + 0.5 * h * k1, x + 0.5 * h, h/2)
    k3 = f(y + 0.5 * h * k2, x + 0.5 * h, h/2)
    k4 = f(y + h * k3, x + h, h)
    return y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)

def f(x, y, h):
    """
    Define the ODE dy/dx = x + y.
    
    Parameters:
    - x: Current value of x
    - y: Initial value of y
    - h: Step size
    
    Returns:
    - dy/dx: Value of y after each step
    """
    return x + y

# Initial condition and time
y0 = 1
x0 = 0
h = 0.1
t_end = 2

# Solve the ODE using RK4 method
y = rk4(y0, x0, h)

# Find y(0.2)
y_0_2 = rk4(y, x0 + t_end * h, h)

print("k1:", y[0])
print("k2:", y[1])
print("k3:", y[2])
print("k4:", y[3])
```

## Oracle Output
Traceback (most recent call last):
  File "C:\Users\SAVYAS~1\AppData\Local\Temp\tmp32kfgzno.py", line 47, in <module>
    print("k1:", y[0])
                 ~^^^
TypeError: 'float' object is not subscriptable


## Student Ledger
```python
import numpy as np

def rk4(y, h):
    k1 = h * (y[0] + 2*y[1]) / 3
    k2 = h * (y[0] + 2*y[1] + 4*y[2]) / 6
    k3 = h * (y[0] + 2*y[1] + 4*y[2] + 2*y[3]) / 6
    k4 = h * (y[0] + 2*y[1] + 4*y[2] + 2*y[3] + y[4]) / 6
    return np.array([k1, k2, k3, k4])

def solve_ode(y0, t, h):
    x = [y0]
    for i in range(len(t) - 1):
        y = rk4(x[-1], h)
        x.append(y[0])
    return x

# Initial conditions
y0 = 1
t = np.linspace(0, 2, 500)

# Solve ODE using RK4 method
solution = solve_ode(y0, t, 0.1)

print(solution)
```