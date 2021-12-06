import numpy as np


def schur_complement(matrix: np.ndarray, complement_size) -> np.ndarray:
    size = matrix.shape[0]
    for row in range(size - complement_size):
        for col in range(size):
            for i in range(size):
                matrix[row, i] /= matrix[row, row]
            for below_row in range(row + 1, size):
                for i in range(size):
                    matrix[below_row, i] -= matrix[row, i] * matrix[below_row, row]
    return matrix


if __name__ == '__main__':
    M = np.random.rand(5,5) * 30 // 1
    print(M)
    schur_complement(M, 2)

