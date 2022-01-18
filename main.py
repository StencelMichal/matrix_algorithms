import copy
import random
from time import time

from sparse_gaussian_elimination import *


def generate_matrix(size, non_zeros):
    matrix = np.zeros((size, size))
    for _ in range(non_zeros):
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)
        val = random.random()
        matrix[x, y] = val
        matrix[y, x] = val
    for i in range(size):
        matrix[i, i] = random.random()

    return matrix


def main():
    m1 = generate_matrix(10**2, 1000)
    # matrix = create_matrix("resources/b.txt")
    matrix = copy.deepcopy(m1)
    cf = CoordinateFormat(matrix)
    draw_nx_graph(SparseGraph(cf))
    start = time()
    cf.gaussian_elimination()
    end = time()

    draw_nx_graph(SparseGraph(cf))
    print(f"time execution sparse: {end - start}\n")

    matrix = copy.deepcopy(m1)
    cf = CoordinateFormat(matrix)
    G = SparseGraph(cf)
    # order = G.cuthil_mckee()
    order = netowrkx_order(G)
    matrix = permute_matrix(matrix, order)
    for i in range(len(matrix)):
        matrix[i, i] = 1
    cf = CoordinateFormat(matrix)
    draw_nx_graph(SparseGraph(cf))
    start = time()
    cf.gaussian_elimination()
    draw_nx_graph(SparseGraph(cf))
    end = time()
    print(f"time execution sparse: {end - start}\n")


if __name__ == '__main__':
    main()
