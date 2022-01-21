import copy
import random
from time import time

from sparse_gaussian_elimination import *


def generate_matrix(size, non_zeros):
    matrix = np.zeros((size, size))
    for _ in range(non_zeros):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        val = random.random()
        matrix[x, y] = val
        matrix[y, x] = val
    for i in range(size):
        matrix[i, i] = random.random()

    return matrix


def main():
    matrix = generate_matrix(300, 1000)
    SparseGraph(matrix).draw()
    cf = CoordinateFormat(matrix)
    start = time()
    cf.gaussian_elimination()
    end = time()
    SparseGraph(cf.dense_matrix()).draw()
    print(f"time execution sparse: {end - start}\n")

    graph = SparseGraph(matrix)
    graph.draw()
    permuted = permute_min_degree(matrix)
    for i in range(len(permuted)):
        permuted[i, i] = 1
    cf = CoordinateFormat(permuted)
    start = time()
    cf.gaussian_elimination()
    end = time()
    SparseGraph(cf.dense_matrix()).draw()
    print(f"time execution sparse: {end - start}\n")


if __name__ == '__main__':
    main()
