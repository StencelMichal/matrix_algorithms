import networkx as nx
import numpy as np
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
        self.neighbours = set()

    def __gt__(self, other):
        return self.degree() > other.degree()

    def degree(self):
        return len(self.neighbours)

    def add_neighbour(self, vertex_id):
        self.neighbours.add(vertex_id)

    def __str__(self):
        return f"id: {self.id} {self.neighbours}"


class SparseGraph:
    def __init__(self, matrix: np.ndarray):
        size = matrix.shape[0]
        self.vertices = {id: Vertex(id) for id in range(size)}

        for col_id, column in enumerate(matrix):
            for row_id, value in enumerate(column):
                if value != 0:
                    self.vertices[row_id].add_neighbour(col_id)
                    self.vertices[col_id].add_neighbour(row_id)

    def min_degree_ordering(self):
        def remove_vertex(v):
            for u in vertices[v.id].neighbours:
                vertices[u].neighbours = (vertices[u].neighbours | vertices[v.id].neighbours) - {v.id}
            del vertices[v.id]

        order = []
        vertices = self.vertices.copy()
        for _ in range(len(vertices)):
            v = min(vertices.values())
            remove_vertex(v)
            order.append(v.id)

        return order

    def draw(self):
        graph = nx.Graph()

        for v in self.vertices.values():
            for u in v.neighbours:
                if v.id != u:
                    graph.add_edge(v.id, u)
        print("number of edges", len(graph.edges))

        nx.draw(graph, with_labels=True)
        plt.show()


def permute(matrix: np.ndarray, order):
    new_matrix = []
    for row in order:
        new_matrix.append(matrix[row])
    return np.array(new_matrix)


def permute_min_degree(matrix: np.ndarray):
    return permute(matrix, SparseGraph(matrix).min_degree_ordering())


def dense_gaussian_elimination(matrix):
    assert matrix.shape[0] == matrix.shape[1]
    size = matrix.shape[0]
    for col1 in range(size - 1):
        factors = [matrix[row][col1] / matrix[col1][col1] for row in range(col1 + 1, size)]
        for col2 in range(col1, size):
            for row in range(col1 + 1, size):
                matrix[row][col2] = matrix[row][col2] - (matrix[col1][col2] * factors[row - col1 - 1])

    return matrix

