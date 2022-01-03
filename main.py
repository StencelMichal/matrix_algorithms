import copy
from time import time
from read import create_matrix
from sparse_gaussian_elimination import gaussian_elimination
from sparse_gaussian_elimination import CoordinateFormat
from guppy import hpy

import importer
from matrix_multiplication import block_matrix_multiplication
from schur_complement import schur_complement
from sparse_matrix_multiplication import Csc
from sparse_matrix_multiplication import csc_multiplication




def main():

    matrix = create_matrix("b.txt")
    h = hpy()
    h.setref()
    h1 = h.heap()
    b = copy.deepcopy(matrix)
    start = time()
    gaussian_elimination(b)
    end = time()
    h2 = h.heap()
    print(f"time execution dense: {end - start}\n")
    print(f"memory usage: {h2.size - h1.size} bytes")

    matrix = create_matrix("b.txt")
    cf = CoordinateFormat(matrix)
    h = hpy()
    h.setref()
    h1 = h.heap()
    print(h1)
    start = time()
    cf.gaussian_elimination()
    end = time()
    h2 = h.heap()
    print(h2)
    print(f"time execution sparse: {end - start}\n")
    print(f"memory usage: {h2.size - h1.size} bytes")





if __name__ == '__main__':
    main()
