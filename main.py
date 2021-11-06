import importer
from matrix_multiplication import block_matrix_multiplication
from time import time

if __name__ == '__main__':
    A = importer.read_file('iga.txt')
    B = importer.read_file('riga.txt')
    A_resized = importer.resize_matrix(A, 2 ** 10)
    B_resized = importer.resize_matrix(B, 2 ** 10)


    block_sizes = [2 ** power for power in range(1, 11)]
    print(block_sizes)
    iteration_orders = ["IJK", "JIK", "IKJ", "JKI", "KIJ", "KJI"]
    with open("results2.txt", "w") as f:
        for block_size in block_sizes:
            output = f"block size: {block_size}\n"
            print(output)
            f.write(output)
            for iteration_order in iteration_orders:
                output = f"    iteration_order:{iteration_order}\n"
                print(output)
                f.write(output)
                start = time()
                C = block_matrix_multiplication(A_resized, B_resized, iteration_order,
                                                (block_size, block_size, block_size))
                end = time()
                output = f"    time execution: {end - start}\n\n"
                print(output)
                f.write(output)
