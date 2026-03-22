# Problem: Use Newton-Raphson to find the square root of 2, starting with x0=1.5. Perform 3 iterations.

## Python Code
```python
import math

def newton_raphson_sqrt(x0, max_iterations):
    for _ in range(max_iterations):
        x = x0 - (x0 ** 2) / (2 * x0)
        if abs(x - int(x)) < 1e-6:
            return round(x, 5)
    return None

# Calculate the square root of 2 using Newton-Raphson method
result = newton_raphson_sqrt(1.5, 3)
print(result)
```

## Ground Truth
None


## Student Ledger
### MATHEMATICAL LEDGER

1. **Problem Analysis**: The B.Tech Math problem asks us to use the Newton-Raphson method to find the square root of 2 starting with \( x_0 = 1.5 \). We need to perform 3 iterations.

2. **Step-by-Step Calculation**:
   - Initialize \( x_0 = 1.5 \).
   - Calculate \( f(x) = (x - 1)^2 \), where \( f(x) \) is the function we want to find.
   - Update \( x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \).

3. **Final Result**: We need to perform 3 iterations and calculate the value of \( x_3 \).
   
4. **Conclusion**: After performing 3 iterations, we get \( x_3 \approx 1.41421356237 \).

### Python Ground Truth

```python
def f(x):
    return (x - 1)**2

def df(x):
    return 2 * (x - 1)

x0 = 1.5
iterations = 3
for _ in range(iterations):
    x_new = x0 - f(x0) / df(x0)
    print(f"Iteration {iterations}: x_new = {x_new}")
    x0 = x_new
```

### Python Ground Truth

```python
def f(x):
    return (x - 1)**2

def df(x):
    return 2 * (x - 1)

x0 = 1.5
iterations = 3
for _ in range(iterations):
    x_new = x0 - f(x0) / df(x0)
    print(f"Iteration {iterations}: x_new = {x_new}")
    x0 = x_new
```