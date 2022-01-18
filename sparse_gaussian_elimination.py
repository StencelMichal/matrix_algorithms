from queue import Queue

import numpy as np

from networkx.utils import reverse_cuthill_mckee_ordering
import networkx as nx
from matplotlib import pyplot as plt


class CoordinateFormat:
    def __init__(self, matrix: np.ndarray):
        self.columns = []
        self.shape = matrix.shape
        for col_id, col in enumerate(matrix.T):
            self.columns.append([(row_id, value) for row_id, value in enumerate(col) if value != 0])

    def __str__(self):
        ret = ""
        for col_id, col in enumerate(self.columns):
            ret += f"col {col_id}: {col}\n"
        return ret

    def gaussian_elimination(self):
        for col1_id, col1 in enumerate(self.columns):
            found = False
            for idx, (row_id, value) in enumerate(col1):
                if row_id == col1_id:
                    found = True
                    on_diagonal = value
                    on_diagonal_idx = idx
                    break
            if not found:
                raise ValueError("0 on diagonal")
            ratios = {row_id: value / on_diagonal for row_id, value in col1[on_diagonal_idx + 1:]}
            for col2 in self.columns[col1_id:]:
                new_elements = False
                col2_values = {col2_id: (idx, value) for idx, (col2_id, value) in enumerate(col2)}
                if col1_id in col2_values:
                    _, subtract_value = col2_values[col1_id]
                    for i in range(col1_id + 1, self.shape[1]):
                        if i in col2_values:
                            idx, _ = col2_values[i]
                            col2[idx] = (col2[idx][0], col2[idx][1] - (subtract_value * ratios.get(i, 0)))
                        else:
                            col2.append((i, - (subtract_value * ratios.get(i, 0))))
                            new_elements = True
                if new_elements:
                    col2.sort(key=lambda x: x[0])

    def dense_matrix(self):
        dense = np.zeros(self.shape)
        for col_id, col in enumerate(self.columns):
            for row_id, value in col:
                dense[row_id, col_id] = value
        return dense


class Vertex:
    def __init__(self, id):
        self.id = id
        self.row = {}
        self.column = {}
        self.visited = False

    def degree(self):
        return len(self.column) + len(self.row)


class SparseGraph:
    def __init__(self, matrix_cf: CoordinateFormat):
        size = len(matrix_cf.columns)
        self.vertices = [Vertex(id) for id in range(size)]

        for col_id, column in enumerate(matrix_cf.columns):
            for row_id, value in column:
                self.vertices[row_id].row[col_id] = value
                self.vertices[col_id].column[row_id] = value

    def cuthil_mckee(self):
        q = Queue(0)
        order = []
        self.vertices.sort(key=lambda v: v.degree())

        for v in self.vertices:
            if not v.visited:
                v.visited = True
                q.put(v)
                while not q.empty():
                    u = q.get()
                    order.append(u.id)
                    children = sorted([self.vertices[i] for i in u.row], key=lambda v: v.degree())
                    for child in children:
                        if not child.visited:
                            child.visited = True
                            q.put(child)

        return order


def gaussian_elimination(matrix):
    assert matrix.shape[0] == matrix.shape[1]
    size = matrix.shape[0]
    for col1 in range(size - 1):
        factors = [matrix[row][col1] / matrix[col1][col1] for row in range(col1 + 1, size)]
        for col2 in range(col1, size):
            for row in range(col1 + 1, size):
                matrix[row][col2] = matrix[row][col2] - (matrix[col1][col2] * factors[row - col1 - 1])

    return matrix


def permute_matrix(matrix: np.ndarray, permutation):
    new_matrix = []
    for row in permutation:
        new_matrix.append(matrix[row])
    return np.array(new_matrix)


def netowrkx_order(G):
    def smallest_degree(G):
        return min(G, key=G.degree)

    new_m = np.zeros((len(G.vertices), len(G.vertices)))
    for v in G.vertices:
        for row, val in v.column.items():
            new_m[row][v.id] = 1
        for col, val in v.row.items():
            new_m[v.id][col] = 1

    G2 = nx.convert_matrix.from_numpy_matrix(new_m)
    order2 = list(reverse_cuthill_mckee_ordering(G2, heuristic=smallest_degree))
    return order2


def draw_nx_graph(G: SparseGraph):
    graph = nx.Graph()

    for v in G.vertices:
        for key, val in v.row.items():
            if v.id != key:
                graph.add_edge(v.id, key)
    print("number of edges", len(graph.edges))

    labelmap = dict(zip(graph.nodes(), [str(i) for i in range(len(G.vertices))]))
    nx.draw(graph, labels=labelmap, with_labels=True)
    plt.show()


if __name__ == '__main__':
    M = (np.random.rand(5, 5) + 0.5) // 1
    print(M)
    matrix_cf = CoordinateFormat(M)
    G = SparseGraph(matrix_cf)
    draw_nx_graph(G)
    order = G.cuthil_mckee()
    for v in G.vertices:
        print(v.degree(), v.column, v.row)
    print("ORDER", order)
    reordered = permute_matrix(M, order)
    print(reordered)

    print(netowrkx_order(G))
