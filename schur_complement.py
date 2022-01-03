import numpy as np

def schur_complement(matrix: np.ndarray, complement_size) -> np.ndarray:
    size = matrix.shape[0]
    for row in range(size - complement_size):
        for i in range(size):
            matrix[row, i] /= matrix[row, row]
        for below_row in range(row + 1, size):
            for i in range(size):
                matrix[below_row, i] -= matrix[row, i] * matrix[below_row, row]
    return matrix


