import struct
import numpy as np


def bto(s, t):
    return struct.unpack(t, s)[0]


# with open("b.txt", "br") as f:
#     r = bto(f.read(4), 'i')
#     c = bto(f.read(4), 'i')
#
#     m = []
#     for i in range(r):
#         vec = []
#         for j in range(c):
#             vec.append(bto(f.read(8), 'd'))
#         m.append(vec)
#
#     arr = np.array(m)
#     plt.spy(arr)
#     plt.show()

def create_matrix(filename):
    with open(filename, "br") as f:
        r = bto(f.read(4), 'i')
        c = bto(f.read(4), 'i')

        m = []
        for i in range(r):
            vec = []
            for j in range(c):
                vec.append(bto(f.read(8), 'd'))
            m.append(vec)

        return np.array(m)
