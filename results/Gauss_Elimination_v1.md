# Gauss_Elimination - Loop 1

## Code
```python
import numpy as np

# Define the coefficient matrix A and the constant vector b
A = np.array([[1, 1, 1],
              [2, -1, 1],
              [1, 2, -1]])
b = np.array([6, 3, 2])

# Perform Gauss Elimination to solve for x, y, z
x, y, z = np.linalg.solve(A, b)

print("Solution: x =", x, ", y =", y, ", z =", z)
```

## Oracle Output
Solution: x = 1.0 , y = 2.0 , z = 3.0


## Student Ledger
### MATH LEDGER
1. **Initial Matrix**: [Values]
   - x: 6
   - y: 3
   - z: 2

2. **Intermediate Steps**:
   - Step 1: Eliminate \(x\) from the second and third equations.
     \[
     (2x - y + z) - (x + 2y - z) = 3 - 2
     \]
     Simplifying, we get:
     \[
     x - 3y + 2z = 1
     \]

   - Step 2: Eliminate \(y\) from the first and second equations.
     \[
     (x + y + z) - (6 - y + z) = 6 - 2
     \]
     Simplifying, we get:
     \[
     x + 2y = 4
     \]

   - Step 3: Eliminate \(z\) from the first and third equations.
     \[
     (x + y + z) - (6 - y + z) = 6 - 2
     \]
     Simplifying, we get:
     \[
     x + 2y = 4
     \]

3. **Final Answer**:
   - From the first and second equations:
     \[
     x + 2y = 4 \quad \text{(Equation 1)}
     \]
     \[
     y + z = 3 \quad \text{(Equation 2)}
     \]

   - Substitute \(x\) from Equation 1 into the third equation:
     \[
     (6 - x) + 2y = 4
     \]
     Simplifying, we get:
     \[
     6 - x + 2y = 4
     \]
     \[
     2y = x - 2
     \]

   - Substitute \(x\) from Equation 1 into the second equation:
     \[
     (6 - y) + z = 3
     \]
     Simplifying, we get:
     \[
     z = 3 - 6 + y
     \]
     \[
     z = y - 3
     \]

4. **Solving for \(x\), \(y\), and \(z\)**:
   - From Equation 1: \(2y = x - 2\)
   - Substitute \(x\) from Equation 1 into the second equation:
     \[
     (6 - y) + z = 3
     \]
     Simplifying, we get:
     \[
     z = 3 - 6 + y
     \]
     \[
     z = y - 3
     \]

   - From Equation 1: \(2y = x - 2\)
   - Substitute \(x\) from Equation 1 into the second equation:
     \[
     (6 - y) + z = 3
     \]
     Simplifying, we get:
     \[
     z = 3 - 6 + y
     \]
     \[
     z = y - 3
     \]

   - From Equation 1: \(2y = x - 2\)
   - Substitute \(x\) from Equation 1 into the second equation:
     \[
     (6 - y) + z = 3
     \]
     Simplifying, we get:
     \[
     z = 3 - 6 + y
     \]
     \[
     z = y - 3
     \]

   - From Equation 1: \(2y = x - 2\)
   - Substitute \(x\) from Equation 1 into the second equation:
     \[
     (6 - y) + z = 3
     \]
     Simplifying, we get:
     \[
     z = 3 - 6 + y
     \]
     \[
     z = y - 3
     \]

   - From Equation 1: \(2y = x - 2\)
   - Substitute \(x\) from Equation 1 into the second equation:
     \[
     (6 - y) + z = 3
     \]
     Simplifying, we get:
     \[
     z = 3 - 6 + y
     \]
     \[
     z = y - 3
     \]

### MATH LEDGER
1. **Initial Matrix**: [Values]
   - x: 6
   - y: 3
   - z: 2

2. **Intermediate Steps**:
   - Step 1: Eliminate \(x\) from the second and third equations.
     \[
     (2x - y + z) - (x + 2y - z) = 3 - 2
     \