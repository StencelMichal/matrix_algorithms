import numpy as np

def matrix_multiplication(A, B, iteration_order):
    len_i = A.shape[0]
    len_k = A.shape[1]
    len_j = B.shape[1]

    C = np.zeros((len_i, len_j))

    match iteration_order.upper():
        case 'IJK':
            for i in range(len_i):
                for j in range(len_j):
                    for k in range(len_k):
                        C[i, j] += A[i, k] * B[k, j]
        case 'JIK':
            for j in range(len_j):
                for i in range(len_i):
                    for k in range(len_k):
                        C[i, j] += A[i, k] * B[k, j]
        case 'IKJ':
            for i in range(len_i):
                for k in range(len_k):
                    for j in range(len_j):
                        C[i, j] += A[i, k] * B[k, j]
        case 'JKI':
            for j in range(len_j):
                for k in range(len_k):
                    for i in range(len_i):
                        C[i, j] += A[i, k] * B[k, j]
        case 'KIJ':
            for k in range(len_k):
                for i in range(len_i):
                    for j in range(len_j):
                        C[i, j] += A[i, k] * B[k, j]
        case 'KJI':
            for k in range(len_k):
                for j in range(len_j):
                    for i in range(len_i):
                        C[i, j] += A[i, k] * B[k, j]

    return C

def block_matrix_multiplication(A, B, iteration_order, block_size):
    len_i = A.shape[0]
    len_k = A.shape[1]
    len_j = B.shape[1]

    C = np.zeros((len_i, len_j))

    size_I, size_K, size_J = block_size

    if len_i % size_I != 0 or len_k % size_K != 0 or len_j % size_J != 0:
        raise ValueError("Block size not compatible with size of matrix")

    match iteration_order.upper():
        case 'IJK':
            for i in range(0, len_i, size_I):
                print(i)
                for j in range(0, len_j, size_J):
                    for k in range(0, len_k, size_K):
                        A_block = A[i:i + size_I, k:k + size_K]
                        B_block = B[k:k + size_K, j:j + size_J]
                        C[i:i + size_I, j:j + size_J] += matrix_multiplication(A_block, B_block, iteration_order)
        case 'JIK':
            for j in range(0, len_j, size_J):
                for i in range(0, len_i, size_I):
                    for k in range(0, len_k, size_K):
                        A_block = A[i:i + size_I, k:k + size_K]
                        B_block = B[k:k + size_K, j:j + size_J]
                        C[i:i + size_I, j:j + size_J] += matrix_multiplication(A_block, B_block, iteration_order)
        case 'IKJ':
            for i in range(0, len_i, size_I):
                for k in range(0, len_k, size_K):
                    for j in range(0, len_j, size_J):
                        A_block = A[i:i + size_I, k:k + size_K]
                        B_block = B[k:k + size_K, j:j + size_J]
                        C[i:i + size_I, j:j + size_J] += matrix_multiplication(A_block, B_block, iteration_order)
        case 'JKI':
            for j in range(0, len_j, size_J):
                for k in range(0, len_k, size_K):
                    for i in range(0, len_i, size_I):
                        A_block = A[i:i + size_I, k:k + size_K]
                        B_block = B[k:k + size_K, j:j + size_J]
                        C[i:i + size_I, j:j + size_J] += matrix_multiplication(A_block, B_block, iteration_order)
        case 'KIJ':
            for k in range(0, len_k, size_K):
                for i in range(0, len_i, size_I):
                    for j in range(0, len_j, size_J):
                        A_block = A[i:i + size_I, k:k + size_K]
                        B_block = B[k:k + size_K, j:j + size_J]
                        C[i:i + size_I, j:j + size_J] += matrix_multiplication(A_block, B_block, iteration_order)
        case 'KJI':
            for k in range(0, len_k, size_K):
                for j in range(0, len_j, size_J):
                    for i in range(0, len_i, size_I):
                        A_block = A[i:i + size_I, k:k + size_K]
                        B_block = B[k:k + size_K, j:j + size_J]
                        C[i:i + size_I, j:j + size_J] += matrix_multiplication(A_block, B_block, iteration_order)

    return C


if __name__ == '__main__':
    A = np.random.rand(25, 25)
    B = np.random.rand(25, 16)

    print(f"Is equal ? : {np.allclose(block_matrix_multiplication(A, B, 'kij', (5, 5, 4)), A @ B)}")
