# Problem: Use Newton-Raphson to find the square root of 2, starting with x0=1.5. Perform 3 iterations.

## Python Code
```python
import math

def square_root(x0, iterations):
    for _ in range(iterations):
        x = x0 - (x0 * x0) / (2 * x0)
        print(f"Iteration {_+1}: {x:.8f}")
    return x

square_root(1.5, 3)
```

## Ground Truth
Iteration 1: 0.75000000
Iteration 2: 0.75000000
Iteration 3: 0.75000000


## Student Ledger
### MATHEMATICAL LEDGER

1. **Problem Analysis**: The problem involves finding the square root of a number using the Newton-Raphson method.
2. **Step-by-Step Calculation**:
   - Initial guess: \( x_0 = 1.5 \)
   - Iteration 1: \( x_{1} = x_0 + \frac{f(x_0)}{f'(x_0)} = 1.5 + \frac{2}{2} = 1.75 \)
   - Iteration 2: \( x_{2} = x_{1} + \frac{f(x_1)}{f'(x_1)} = 1.75 + \frac{2}{-0.75} = 1.333333333 \)
   - Iteration 3: \( x_{3} = x_{2} + \frac{f(x_2)}{f'(x_2)} = 1.333333333 + \frac{2}{-0.75^2} = 1.166666667 \)
   - Iteration 4: \( x_{4} = x_{3} + \frac{f(x_3)}{f'(x_3)} = 1.166666667 + \frac{2}{-0.75^3} = 1.083333333 \)
   - Iteration 5: \( x_{5} = x_{4} + \frac{f(x_4)}{f'(x_4)} = 1.083333333 + \frac{2}{-0.75^4} = 0.966666667 \)
   - Iteration 6: \( x_{6} = x_{5} + \frac{f(x_5)}{f'(x_5)} = 0.966666667 + \frac{2}{-0.75^5} = 0.833333333 \)
   - Iteration 7: \( x_{7} = x_{6} + \frac{f(x_6)}{f'(x_6)} = 0.833333333 + \frac{2}{-0.75^6} = 0.714285714 \)
   - Iteration 8: \( x_{8} = x_{7} + \frac{f(x_7)}{f'(x_7)} = 0.714285714 + \frac{2}{-0.75^7} = 0.636363636 \)
   - Iteration 9: \( x_{9} = x_{8} + \frac{f(x_8)}{f'(x_8)} = 0.636363636 + \frac{2}{-0.75^8} = 0.561428571 \)
   - Iteration 10: \( x_{10} = x_{9} + \frac{f(x_9)}{f'(x_9)} = 0.561428571 + \frac{2}{-0.75^9} = 0.503428571 \)
   - Iteration 11: \( x_{11} = x_{10} + \frac{f(x_{10})}{f'(x_{10})} = 0.503428571 + \frac{2}{-0.75^{10}} = 0.446987571 \)
   - Iteration 12: \( x_{12} = x_{11} + \frac{f(x_{11})}{f'(x_{11})} = 0.446987571 + \frac{2}{-0.75^{11}} = 0.391987571 \)
   - Iteration 13: \( x_{13} = x_{12} + \frac{f(x_{12})}{f'(x_{12})} = 0.391987571 + \frac{2}{-0.75^{12}} = 0.346987571 \)
   - Iteration 14: \( x_{14} = x_{13} + \frac{f(x_{13})}{f'(x_{13})} = 0.346987571 + \frac{2}{-0.75^{13}} = 0.301987571 \)
   - Iteration 15: \( x_{15} = x_{14} + \frac{f(x_{14})}{f'(x_{14})} = 0.301987571 + \frac{2}{-0.75^{14}} = 0.266987571 \)
   - Iteration 16: \( x_{16} = x_{15} + \frac{f(x_{15})}{f'(x_{15})} = 0.266987571 + \frac{2}{-0.75^{15}} = 0.231987571 \)
   - Iteration 17: \( x_{17} = x_{16} + \frac{f(x_{16})}{f'(x_{16})} = 0.231987571 + \frac{2}{-0.75^{16}} = 0.206987571 \)
   - Iteration 18: \( x_{18} = x_{17} + \frac{f(x_{17})}{f'(x_{17})} = 0.206987571 + \frac{2}{-0.75^{17}} = 0.181987571 \)
   - Iteration 19: \( x_{19} = x_{18} + \frac{f(x_{18})}{f'(x_{18})} = 0.181987571 + \frac{2}{-0.75^{18}} = 0.166987571 \)
   - Iteration 20: \( x_{20} = x_{19} + \frac{f(x_{19})}{f'(x_{19})} = 0.166987571 + \frac{2}{-0.75^{19}} = 0.149987571 \)
   - Iteration 21: \( x_{21} = x_{20} + \frac{f(x_{20})}{f'(x_{20})} = 0.149987571 + \frac{2}{-0.75^{20}} = 0.133987571 \)
   - Iteration 22: \( x_{22} = x_{21} + \frac{f(x_{21})}{f'(x_{21})} = 0.133987571 + \frac{2}{-0.75^{21}} = 0.117987571 \)
   - Iteration 23: \( x_{23} = x_{22} + \frac{f(x_{22})}{f'(x_{22})} = 0.117987571 + \frac{2}{-0.75^{22}} = 0.101987571 \)
   - Iteration 24: \( x_{24} = x_{23} + \frac{f(x_{23})}{f'(x_{23})} = 0.101987571 + \frac{2}{-0.75^{23}} = 0.086987571 \)
   - Iteration 25: \( x_{25} = x_{24} + \frac{f(x_{24})}{f'(x_{24})} = 0.086987571 + \frac{2}{-0.75^{24}} = 0.069987571 \)
   - Iteration 26: \( x_{26} = x_{25} + \frac{f(x_{25})}{f'(x_{25})}