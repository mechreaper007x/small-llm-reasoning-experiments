# Problem: Find the determinant and inverse of the matrix [[1, 2], [3, 4]].

## Python Code
```python
import numpy as np

# Define the matrix
matrix = [[1, 2], [3, 4]]

# Calculate the determinant and inverse using NumPy
det = np.linalg.det(matrix)
inv_matrix = np.linalg.inv(matrix)

print("Determinant:", det)
print("Inverse Matrix:")
print(inv_matrix)
```

## Ground Truth
Determinant: -2.0000000000000004
Inverse Matrix:
[[-2.   1. ]
 [ 1.5 -0.5]]


## Student Ledger
### MATHEMATICAL LEDGER

1. **Problem Analysis**: The problem involves finding the determinant and inverse of a given matrix using Python's `numpy` library.

2. **Step-by-Step Calculation**:
   - Determinant calculation: Using `numpy.linalg.det`, we get `-2`.
   - Inverse Matrix calculation: Using `numpy.linalg.inv`, we get \(\left[\begin{array}{cc} -2 & 1 \\ 1.5 & -0.5 \end{array}\right]\).

3. **Final Result**: The determinant is `-2` and the inverse matrix is \(\left[\begin{array}{cc}-2 & 1 \\ 1.5 & -0.5\end{array}\right]\).

4. **Conclusion**: 
   - The determinant is correct but misleadingly reported as `-2`.
   - The inverse matrix is correctly calculated and matches the ground truth.

**Logic/Proof**: 
- The student's calculation of the determinant using `numpy.linalg.det` yields `-2`, which is mathematically correct.
- The student's calculation of the inverse matrix using `numpy.linalg.inv` gives \(\left[\begin{array}{cc}-2 & 1 \\ 1.5 & -0.5\end{array}\right]\), which matches the ground truth.

**Advisor Feedback**: 
- The student's determinant calculation is correct in principle but misleadingly reported due to floating-point precision.
- The inverse matrix is calculated correctly and matches the ground truth, though it is not exact as expected for a B.Tech-level answer.