import numpy as np

def manual_matrix_multiplication(A,B):
    # Get dimensions
    m, n = A.shape
    n_check, p = B.shape
    
    # Verify if multiplication is possible
    if n != n_check:
        raise ValueError("Matrices dimensions don't match for multiplication!")

    # Initialize result matrix with zeros
    C = np.zeros((m, p))

    # Triple nested loop logic
    for i in range(m):          # Iterate through rows of A
        for j in range(p):      # Iterate through columns of B
            for k in range(n):  # Dot product summation
                C[i, j] += A[i, k] * B[k, j]
    return C

# Example usage:
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(manual_matrix_multiplication(A, B))


def vectorized_scratch_multiplication(A, B):
    m, n = A.shape
    _, p = B.shape
    C = np.zeros((m, p))

    for i in range(m):
        for j in range(p):
            # Vectorized dot product of row i and column j
            C[i, j] = np.sum(A[i, :] * B[:, j])
    return C

# Example usage:
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(vectorized_scratch_multiplication(A, B))