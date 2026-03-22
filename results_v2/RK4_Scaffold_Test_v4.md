# Loop 4

## Absolute Truth
Step-by-step RK4 results with h = 0.1:

Step 1: x = 0.0 -> x = 0.0
k1 = 0.010000
k2 = 0.010100
k3 = 0.010100
k4 = 0.010201
y_new = 1.010100

Step 2: x = 0.0 -> x = 0.0
k1 = 0.010201
k2 = 0.010302
k3 = 0.010303
k4 = 0.010404
y_new = 1.020403

Step 3: x = 0.0 -> x = 0.0
k1 = 0.010404
k2 = 0.010506
k3 = 0.010507
k4 = 0.010609
y_new = 1.030909

Step 4: x = 0.0 -> x = 0.0
k1 = 0.010609
k2 = 0.010712
k3 = 0.010713
k4 = 0.010816
y_new = 1.041622

Step 5: x = 0.0 -> x = 0.1
k1 = 0.010816
k2 = 0.010920
k3 = 0.010921
k4 = 0.011025
y_new = 1.052542

Step 6: x = 0.1 -> x = 0.1
k1 = 0.011025
k2 = 0.011131
k3 = 0.011131
k4 = 0.011237
y_new = 1.063673

Step 7: x = 0.1 -> x = 0.1
k1 = 0.011237
k2 = 0.011343
k3 = 0.011343
k4 = 0.011450
y_new = 1.075016

Step 8: x = 0.1 -> x = 0.1
k1 = 0.011450
k2 = 0.011557
k3 = 0.011558
k4 = 0.011666
y_new = 1.086574

Step 9: x = 0.1 -> x = 0.1
k1 = 0.011666
k2 = 0.011774
k3 = 0.011775
k4 = 0.011883
y_new = 1.098349

Step 10: x = 0.1 -> x = 0.1
k1 = 0.011883
k2 = 0.011993
k3 = 0.011993
k4 = 0.012103
y_new = 1.110342

Step 11: x = 0.1 -> x = 0.1
k1 = 0.012103
k2 = 0.012214
k3 = 0.012214
k4 = 0.012326
y_new = 1.122556

Step 12: x = 0.1 -> x = 0.1
k1 = 0.012326
k2 = 0.012437
k3 = 0.012438
k4 = 0.012550
y_new = 1.134994

Step 13: x = 0.1 -> x = 0.1
k1 = 0.012550
k2 = 0.012663
k3 = 0.012663
k4 = 0.012777
y_new = 1.147657

Step 14: x = 0.1 -> x = 0.1
k1 = 0.012777
k2 = 0.012890
k3 = 0.012891
k4 = 0.013005
y_new = 1.160548

Step 15: x = 0.1 -> x = 0.1
k1 = 0.013005
k2 = 0.013121
k3 = 0.013121
k4 = 0.013237
y_new = 1.173668

Step 16: x = 0.1 -> x = 0.2
k1 = 0.013237
k2 = 0.013353
k3 = 0.013353
k4 = 0.013470
y_new = 1.187022

Step 17: x = 0.2 -> x = 0.2
k1 = 0.013470
k2 = 0.013588
k3 = 0.013588
k4 = 0.013706
y_new = 1.200610

Step 18: x = 0.2 -> x = 0.2
k1 = 0.013706
k2 = 0.013825
k3 = 0.013825
k4 = 0.013944
y_new = 1.214435

Step 19: x = 0.2 -> x = 0.2
k1 = 0.013944
k2 = 0.014064
k3 = 0.014065
k4 = 0.014185
y_new = 1.228499

Step 20: x = 0.2 -> x = 0.2
k1 = 0.014185
k2 = 0.014306
k3 = 0.014307
k4 = 0.014428
y_new = 1.242806

Final answer for y(0.2):
y(0.2) = 1.242806

Verification with smaller step size (h = 0.01):
y(0.2) = 1.242806

## Strategy
To solve the given ODE using the RK4 method, we need to follow these steps:

1. **Define the ODE**: The equation is \( \frac{dy}{dx} = x + y \).
2. **Initial Conditions and Step Size**: We have initial conditions \( y(0) = 1 \) and step size \( h = 0.1 \).
3. **RK4 Method Implementation**:
   - Calculate the first derivative at each step using the formula: 
     \[
     k1 = f(x, y) = x + y
     \]
     \[
     k2 = f(x + \frac{h}{2}, y + \frac{k1}{2}) = (x + \frac{h}{2} + y + \frac{k1}{2}) + (y + \frac{k1}{2})
     \]
   - Calculate the second derivative at each step using the formula:
     \[
     k3 = f(x + \frac{h}{2}, y + \frac{k2}{2}) = (x + \frac{h}{2} + y + \frac{k2}{2}) + (y + \frac{k2}{2})
     \]
     \[
     k4 = f(x + h, y + \frac{k3}{2}) = (x + h + y + \frac{k3}{2}) + (y + \frac{k3}{2})
     \]

   - Update the solution using the formula:
     \[
     x_{n+1} = x_n + h
     \]
     \[
     y_{n+1} = y_n + k1
     \]
     \[
     y_{n+1} = y_{n+1} + k2
     \]
     \[
     y_{n+1} = y_{n+1} + k3
     \]
     \[
     y_{n+1} = y_{n+1} + k4
     \]

   - Repeat the process for each step until \( x_n = 0.2 \).

4. **Final Answer**: The value of \( y(0.2) \) can be found by following the steps above.

**Mathematical Strategy**:
- Start with the initial conditions and the step size.
- Calculate the first derivative at each step using the formula for RK4.
- Update the solution using the formula for RK4.
- Repeat the process until \( x_n = 0.2 \).

This strategy ensures that we accurately compute the solution to the ODE using the RK4 method with a specified step size.

## Submitted Code
```python
import numpy as np

def rk4(y, h):
    k1 = f(x, y)
    k2 = f(x + (h/2), y + (k1 + 0.5 * k2))
    k3 = f(x + (h/2), y + (k2 + 0.5 * k3))
    k4 = f(x + h, y + (k3 + 0.5 * k4))
    return x + (h/6) * (k1 + 2*k2 + 2*k3 + k4)

def f(x, y):
    return x + y

x = 0
y = 1
h = 0.1
n = int((np.pi - x)/h)
for i in range(n):
    x = x + h
    y = rk4(y, h)
print(f'y(0.2) = {y:.6f}')
```

## Output
Traceback (most recent call last):
  File "C:\Users\SAVYAS~1\AppData\Local\Temp\tmpqaob088l.py", line 19, in <module>
    y = rk4(y, h)
        ^^^^^^^^^
  File "C:\Users\SAVYAS~1\AppData\Local\Temp\tmpqaob088l.py", line 5, in rk4
    k2 = f(x + (h/2), y + (k1 + 0.5 * k2))
                                      ^^
UnboundLocalError: cannot access local variable 'k2' where it is not associated with a value

## Surgical Audit
{
  "status": "FAILURE",
  "surgical_feedback": [
    {
      "line": 5,
      "change": "k2 = f(x + (h/2), y + (k1 * h/2))",
      "because": "The calculation for `k2` incorrectly references `k2` itself in the argument. The correct formula for RK4's `k2` is `f(x + h/2, y + k1 * h/2)`. The same error exists in lines 6 and 7 for `k3` and `k4`. The units and structure of the slope calculations are wrong: slopes (`k1`, `k2`, etc.) should be multiplied by `h` when updating `y`. The return statement also incorrectly updates `x` instead of `y`."
    },
    {
      "line": 6,
      "change": "k3 = f(x + (h/2), y + (k2 * h/2))",
      "because": "Same error as above: `k3` incorrectly references itself and lacks proper scaling by `h`."
    },
    {
      "line": 7,
      "change": "k4 = f(x + h, y + (k3 * h))",
      "because": "Same error as above: `k4` incorrectly references `k4` and lacks proper scaling by `h`."
    },
    {
      "line": 8,
      "change": "return y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)",
      "because": "The return statement incorrectly updates `x` instead of `y` and lacks proper scaling of slopes by `h`."
    }
  ],
  "survival_score": 2
}