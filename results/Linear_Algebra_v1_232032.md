# Problem: Find the determinant and inverse of the matrix [[1, 2], [3, 4]].

## Python Code
```python
import numpy as np

# Define the matrix
matrix = np.array([[1, 2], [3, 4]])

# Calculate the determinant
det = np.linalg.det(matrix)

# Calculate the inverse
inv = np.linalg.inv(matrix)

# Print intermediate steps and final answer
print("Determinant:", det)
print("Inverse:", inv)
```

## Ground Truth
Determinant: -2.0000000000000004
Inverse: [[-2.   1. ]
 [ 1.5 -0.5]]


## Student Ledger
### MATHEMATICAL LEDGER

1. **Problem Analysis**: The given matrix is a 2x2 identity matrix, and the determinant of an identity matrix is always 1.
2. **Step-by-Step Calculation**:
   - Determinant: \( \det\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = 1 \times 4 - 2 \times 3 = 4 - 6 = -2 \).
   - Inverse: The inverse of an identity matrix is also the same as the original matrix, so the inverse of \(\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\) is \(\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\).
3. **Final Result**: Determinant: -2
   - Inverse: \[\boxed{\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}}\]

4. **Conclusion**: The determinant of the matrix is \(-2\) and its inverse is also \(\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\).