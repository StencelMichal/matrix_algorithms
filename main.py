import importer
from matrix_multiplication import block_matrix_multiplication
from matrix_multiplication import matrix_multiplication
from time import time
from matplotlib import pyplot as plt


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
    A_resized = importer.resize_matrix(A, 2 ** 10)
    B_resized = importer.resize_matrix(B, 2 ** 10)

    show_non_zero_scatter(A)
    show_non_zero_scatter(B)
    show_non_zero_scatter(matrix_multiplication(A, B, 'IJK'))

    # DIFFERENT ITERATION ORDERS
    iteration_orders = ["IJK", "JIK", "IKJ", "JKI", "KIJ", "KJI"]
    with open("results_different_loops.txt", "w") as f:
        for iteration_order in iteration_orders:
            output = f"iteration_order: {iteration_order}\n"
            print(output)
            f.write(output)
            start = time()
            matrix_multiplication(A_resized, B_resized, iteration_order)
            end = time()
            output = f"time execution: {end - start}\n"
            print(output)
            f.write(output)

    # DIFFERENT SIZES OF BLOCKS
    block_sizes = [2 ** power for power in range(1, 11)]
    with open("results_different_blocks.txt", "w") as f:
        for block_size in block_sizes:
            output = f"block size: {block_size}\n"
            print(output)
            f.write(output)
            start = time()
            block_matrix_multiplication(A_resized, B_resized, iteration_order, (block_size, block_size, block_size))
            end = time()
            output = f"time execution: {end - start}\n"
            print(output)
            f.write(output)


if __name__ == '__main__':
    main()
