import random

import numpy as np


def read_file(filename: str) -> np.ndarray:
    with open(filename, 'r') as f:
        ndims = list(map(int, f.readline().split()))

        matrix = np.empty(ndims, dtype=float)

        for line in f:
            if line == '\n':
                break
            x, y, val = list(line.split())
            x = int(x)
            y = int(y)
            val = float(val)
            matrix[x - 1, y - 1] = val

    return matrix


def resize_matrix(matrix: np.ndarray, desired_size: int) -> np.ndarray:
    new_matrix = np.zeros((desired_size, desired_size), dtype=float)
    block_size = matrix.shape[0]
    times = desired_size // block_size
    for i in range(times):
        for j in range(times):
            new_matrix[i * block_size: (1 + i) * block_size,
            j * block_size: (j + 1) * block_size] = matrix * random.randint(2, 100)
    return new_matrix
