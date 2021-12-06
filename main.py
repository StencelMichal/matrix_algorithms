from time import time

from matplotlib import pyplot as plt

import importer
from schur_complement import schur_complement


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
    execute('fem.txt')


def execute(filename):
    M = importer.read_file(filename)
    for complement_ratio in [0.5, 0.25, 0.125, 0.0625]:
        with open("result_" + filename.strip(".txt") + "_" + str(complement_ratio), "w") as f:
            for power in range(4, 9):
                M_resized = importer.resize_matrix(M, 2 ** power)
                complement_size = int(M_resized.shape[0] * complement_ratio)
                output = f"matrix size: {2 ** power}x{2 ** power}\n"
                f.write(output)
                print(output)
                start = time()
                schur_complement(M_resized, complement_size)
                end = time()
                output = f"time execution: {end - start}\n"
                f.write(output)
                print(output)


if __name__ == '__main__':
    main()
