from time import time

from matplotlib import pyplot as plt

import importer
from matrix_multiplication import block_matrix_multiplication
from schur_complement import schur_complement
from sparse_matrix_multiplication import Csc
from sparse_matrix_multiplication import csc_multiplication

def show_non_zero_scatter(matrix):
    matrix_nonzero = abs(matrix) > 1e-3
    X = []
    Y = []
    for row_id, row in enumerate(matrix_nonzero):
        for col_id, field in enumerate(row):
            if field:
                X.append(col_id)
                Y.append(abs(row_id - len(matrix_nonzero)))

    plt.style.use('seaborn')
    plt.scatter(X, Y)
    plt.show()


def main():
    A = importer.read_file('iga.txt')
    B = importer.read_file('riga.txt')
    A = importer.resize_matrix(A, 2 ** 10)
    B = importer.resize_matrix(A, 2 ** 10)

    A_csc = Csc(A)
    B_csc = Csc(B)

    start = time()
    # block_matrix_multiplication(A, B, "JKI", (64, 64, 64))
    csc_multiplication(A_csc, B_csc)
    end = time()
    print(f"time execution: {end - start}\n")




if __name__ == '__main__':
    main()
