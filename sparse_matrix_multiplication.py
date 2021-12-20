import numpy as np


class Csc:
    def __init__(self, matrix: np.ndarray = None):
        self.values = []
        self.rows = []
        self.cols = [0]
        self.rows_amount, self.cols_amount = matrix.shape
        if matrix is not None:
            for col in matrix.T:
                for row_id, value in enumerate(col):
                    if value != 0:
                        self.values.append(value)
                        self.rows.append(row_id)
                self.cols.append(len(self.values))

    def get_column(self, idx):
        start, end = self.cols[idx], self.cols[idx + 1]
        return {(row, idx): val for row, val in zip(self.rows[start: end], self.values[start: end])}


def csc_multiplication(csc_1: Csc, csc_2: Csc) -> np.ndarray:
    assert csc_1.cols_amount == csc_2.rows_amount
    res = np.zeros((csc_1.rows_amount, csc_2.cols_amount))
    for j in range(csc_2.cols_amount):
        column_2 = csc_2.get_column(j)
        for k in range(csc_1.cols_amount):
            if (k, j) in column_2:
                column_1 = csc_1.get_column(k)
                for i in range(csc_1.rows_amount):
                    if (i, k) in column_1:
                        res[i, j] += column_2[(k, j)] * column_1[(i, k)]

    return res

