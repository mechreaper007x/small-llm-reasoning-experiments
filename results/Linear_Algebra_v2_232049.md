# Problem: Find the determinant and inverse of the matrix [[1, 2], [3, 4]].

## Python Code
```python
import numpy as np

# Define the matrix
matrix = np.array([[1, 2], [3, 4]])

# Calculate the determinant and inverse of the matrix
determinant = np.linalg.det(matrix)
inverse_matrix = np.linalg.inv(matrix)

print("Determinant:", determinant)
print("Inverse Matrix:")
print(inverse_matrix)
```

## Ground Truth
Determinant: -2.0000000000000004
Inverse Matrix:
[[-2.   1. ]
 [ 1.5 -0.5]]


## Student Ledger
### MATHEMATICAL LEDGER

#### Problem Analysis:
The problem requires finding the determinant and inverse of a given matrix.

#### Step-by-Step Calculation:
1. **Determinant**: The determinant is calculated using the formula for a \(2 \times 2\) matrix, which is \(\text{det} = (a_{11} \cdot a_{22}) - (a_{12} \cdot a_{21})\).
   For our matrix \([1, 2], [3, 4]\), the determinant is \(1 \cdot 4 - 2 \cdot 3 = 4 - 6 = -2\).

2. **Inverse Matrix**: The inverse of a \(2 \times 2\) matrix can be found using the formula:
   \[
   A^{-1} = \frac{1}{\text{det}(A)} \begin{bmatrix}
   d & -b \\
   -c & a
   \end{bmatrix}
   \]
   For our matrix, this becomes:
   \[
   A^{-1} = \frac{1}{-2} \begin{bmatrix}
   4 & -2 \\
   -3 & 1
   \end{bmatrix} = \begin{bmatrix}
   -2 & 1 \\
   \frac{3}{2} & -\frac{1}{2}
   \end{bmatrix}
   \]

#### Final Result:
- **Determinant**: \(-2.0000000000000004\)
- **Inverse Matrix**:
  \[
  \begin{bmatrix}
  -2 & 1 \\
  \frac{3}{2} & -\frac{1}{2}
  \end{bmatrix}
  \]

#### Conclusion:
The determinant of the matrix is \(-2\) and its inverse is
\[ 
\begin{bmatrix}
-2 & 1 \\
\frac{3}{2} & -\frac{1}{2}
\end{bmatrix}
\]