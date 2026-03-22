# Loop 2

## Absolute Truth
Traceback (most recent call last):
  File "C:\Users\SAVYAS~1\AppData\Local\Temp\tmp1pxzuhpy.py", line 20, in <module>
    x_n, f_xn, f_prime_xn, x_n_plus_1 = newton_raphson_iteration(x_n, f, f_prime)
                                                                 ^^^
NameError: name 'x_n' is not defined

## Strategy
To find a root of \( f(x) = x^3 - x - 2 \) using the Newton-Raphson method with an initial guess \( x_0 = 1.5 \), we need to follow these steps:

### Step-by-Step Solution

#### 1. Define the function and its derivative
The given function is:
\[ f(x) = x^3 - x - 2 \]

First, compute the derivative of \( f(x) \):
\[ f'(x) = 3x^2 - 1 \]

#### 2. Choose an initial guess
We start with \( x_0 = 1.5 \).

#### 3. Perform Newton-Raphson iteration

The formula for the Newton-Raphson method is:
\[ x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \]

Let's perform three iterations:

##### Iteration 1: \( x_0 = 1.5 \)
1. Compute \( f(1.5) \):
   \[ f(1.5) = (1.5)^3 - 1.5 - 2 = 3.375 - 1.5 - 2 = -1.125 \]
   
2. Compute \( f'(1.5) \):
   \[ f'(1.5) = 3(1.5)^2 - 1 = 3(2.25) - 1 = 6.75 - 1 = 5.75 \]

3. Update the guess:
   \[ x_1 = x_0 - \frac{f(x_0)}{f'(x_0)} = 1.5 - \frac{-1.125}{5.75} \approx 1.5 + 0.1843 \approx 1.6843 \]

##### Iteration 2: \( x_1 = 1.6843 \)
1. Compute \( f(1.6843) \):
   \[ f(1.6843) = (1.6843)^3 - 1.6843 - 2 \approx 0.7957 \]
   
2. Compute \( f'(1.6843) \):
   \[ f'(1.6843) = 3(1.6843)^2 - 1 \approx 3(2.828) - 1 = 8.484 - 1 = 7.484 \]

3. Update the guess:
   \[ x_2 = x_1 - \frac{f(x_1)}{f'(x_1)} = 1.6843 - \frac{0.7957}{7.484} \approx 1.6843 - 0.1087 \approx 1.5756 \]

##### Iteration 3: \( x_2 = 1.5756 \)
1. Compute \( f(1.5756) \):
   \[ f(1.5756) = (1.5756)^3 - 1.5756 - 2 \approx -0.0894 \]
   
2. Compute \( f'(1.5756) \):
   \[ f'(1.5756) = 3(1.5756)^2 - 1 \approx 3(2.480) - 1 = 7.440 - 1 = 6.440 \]

3. Update the guess:
   \[ x_3 = x_2 - \frac{f(x_2)}{f'(x_2)} = 1.5756 - \frac{-0.0894}{6.440} \approx 1.5756 + 0.0131 \approx 1.5887 \]

### Final Answer:
- **Final guess**: \( x_3 = 1.5887 \)
- **First iteration**: \( x_2 = 1.5756 \), \( f(x_2) = -0.0894 \), \( f'(x_2) = 6.440 \), \( x_3 = 1.5887 \)
- **Second iteration**: \( x_3 = 1.5756 \), \( f(x_3) = -0.0894 \), \( f'(x_3) = 6.4

## Submitted Code
```python
import numpy as np

# Define the function and its derivative
def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

# Initial guess
x0 = 1.5

# Perform Newton-Raphson iteration
for _ in range(3):
    x_n_plus_1 = x_n - f(x_n) / df(x_n)
    x_n, f_xn, f_prime_xn, x_n_plus_1 = x_n_plus_1, f(x_n), df(x_n), x_n_plus_1

# Print the results
print("Final guess:", x_n_plus_1)
print("First iteration:", x_n, "f(x_n)", f(x_n))
print("Second iteration:", x_n_plus_1, "f(x_n)", f(x_n_plus_1))
```

## Output
Traceback (most recent call last):
  File "C:\Users\SAVYAS~1\AppData\Local\Temp\tmp2bjm3wn6.py", line 15, in <module>
    x_n_plus_1 = x_n - f(x_n) / df(x_n)
                 ^^^
NameError: name 'x_n' is not defined

## Surgical Audit
{
  "status": "FAILURE",
  "surgical_feedback": "Parse Error",
  "survival_score": 0
}