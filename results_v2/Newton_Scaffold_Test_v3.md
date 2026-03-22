# Loop 3

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

def newton_raphson_iteration(x_n, f, f_prime):
    x_n_plus_1 = x_n - (f(x_n) / f_prime(x_n))
    return x_n_plus_1

# Initial guess
x0 = 1.5
iterations = 3

for _ in range(iterations):
    x_n = x0
    for _ in range(2):  # Perform two iterations to get the desired number of steps
        x_n = newton_raphson_iteration(x_n, lambda x: x**3 - x - 2, np.diff(lambda x: x**3 - x - 2))
    print(f"Final guess after {iterations} iterations: {x_n:.6f}")
```

## Output
Traceback (most recent call last):
  File "C:\Users\SAVYAS~1\AppData\Local\Temp\tmp3an42oqo.py", line 27, in <module>
    x_n = newton_raphson_iteration(x_n, lambda x: x**3 - x - 2, np.diff(lambda x: x**3 - x - 2))
                                                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Savyasachi Mishra\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\numpy\lib\_function_base_impl.py", line 1484, in diff
    raise ValueError("diff requires input that is at least one dimensional")
ValueError: diff requires input that is at least one dimensional

## Surgical Audit
{
  "status": "FAILURE",
  "surgical_feedback": "Parse Error",
  "survival_score": 0
}