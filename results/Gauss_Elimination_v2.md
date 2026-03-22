# Gauss_Elimination - Loop 2

## Code
```python
import numpy as np

# Define the system of linear equations
A = np.array([[1, 1, 1], [2, -1, 1], [1, 2, -1]])

# Solve the system using NumPy's linalg.solve function
x, y, z = np.linalg.solve(A, np.array([6, 3, 2]))

print("Final values of x, y, z:", x, y, z)
```

## Oracle Output
Final values of x, y, z: 1.0 2.0 3.0


## Student Ledger
### MATH LEDGER
1. **Initial Matrix**: [Values]
2. **Intermediate Steps**: [Steps from Python]
3. **Final Answer**: [x, y, z] = (1.0, 2.0, 3.0)

**Explanation:**
The given system of linear equations can be represented in matrix form as:
\[ A \mathbf{x} = \mathbf{b} \]

Where:
- \( A \) is the coefficient matrix,
- \( \mathbf{x} \) is the vector of variables (x, y, z),
- \( \mathbf{b} \) is the constant term vector.

The given system is:
\[ 
\begin{align*}
1.0 & + 2.0 + 3.0 = 6 \\
1.0 - 2.0 + 3.0 &= 3 \\
1.0 + 2.0 - 3.0 &= 2
\end{align*}
\]

The matrix \( A \) is:
\[ 
A = \begin{bmatrix} 1 & 2 & 3 \\ 1 & -2 & 3 \\ 1 & 2 & -3 \end{bmatrix}
\]

To solve this system using Gauss Elimination, we perform the following steps:

1. **Eliminate \( x \) from the second and third rows**:
   - Subtract the first row from the second row: 
     \[ 
     R_2 = R_2 - R_1
     \]
     \[
     \begin{bmatrix} 1 & 2 & 3 \\ 0 & -4 & 0 \\ 1 & 2 & -3 \end{bmatrix}
     \]

   - Subtract the first row from the third row:
     \[ 
     R_3 = R_3 - R_1
     \]
     \[
     \begin{bmatrix} 1 & 2 & 3 \\ 0 & -4 & 0 \\ 0 & 0 & -6 \end{bmatrix}
     \]

2. **Eliminate \( y \) from the third row**:
   - Divide the second row by -4:
     \[ 
     R_2 = \frac{R_2}{-4}
     \]
     \[
     \begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 0 \\ 0 & 0 & -6 \end{bmatrix}
     \]

   - Add the second row to the third row:
     \[ 
     R_3 = R_3 + R_2
     \]
     \[
     \begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{bmatrix}
     \]

The matrix \( A \) is now in row echelon form. The system of equations corresponding to this matrix is:
\[ 
\begin{align*}
x + 2y + 3z &= 6 \\
y &= 1 \\
-6z &= -6
\end{align*}
\]

From the third equation, we can solve for \( z \):
\[ 
z = \frac{-6}{-6} = 1
\]

Now substitute \( z = 1 \) into the second row to find \( y \):
\[ 
y = 1 \\
\]
Finally, substitute \( x = -2y + z \) and \( y = 1 \) into this equation:
\[ 
x = -2(1) + 1 = -1
\]

Thus, the solution is:
\[ 
(x, y, z) = (-1, 1, 1)
\]