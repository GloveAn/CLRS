#!/usr/bin/python
from collections import deque


class Vertex():
    def __init__(self, id):
        self.id = id


class Graph():
    def __init__(self, V, E):
        self._vertices = V


    def vertices(self):
        r = []
        for i in self._vertices:
            r.append(self._vertices[i])
        return r


    def neighbors(self, u):
        raise NotImplementedError


class MatrixGraph(Graph):
    def __init__(self, V, E):
        super().__init__(V, E)

        n = len(V)

        self._matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i, j, w in E:
            self._matrix[i][j] = w


    def neighbors(self, u):
        u = u.id
        r = []

        for i in range(len(self._matrix)):
            if self._matrix[u][i]:
                r.append(self._vertices[i])

        return r


class AdjListGraph(Graph):
    def __init__(self, V, E):
        super().__init__(V, E)

        n = len(V)

        self._vertices = V
        self._adj_list = [[] for i in range(n)]
        for i, j, w in E:
            self._adj_list[i].append((j, w))


    def neighbors(self, u):
        u = u.id
        r = []

        for i, w in self._adj_list[u]:
            r.append(self._vertices[i])

        return r


# chapter 22.2, exerceises 22.2-3
# errata: a single bit suffices by removing line 18
def bfs(G, s):
    WHITE = 0
    # BLACK = 1
    GRAY = 2

    INFINITE = 0x7FFFFFFF

    for u in G.vertices():
        if u == s: continue

        u.color = WHITE
        u.d = INFINITE
        u.pi = None
    s.color = GRAY
    s.d = 0
    s.pi = None
    Q = deque()
    Q.append(s)
    while len(Q):
        u = Q.popleft()
        for v in G.neighbors(u):
            if v.color == WHITE and v.pi is None:
                v.color = GRAY
                v.d = u.d + 1
                v.pi = u
                Q.append(v)
        # u.color = BLACK


def print_path(G, s, v):
    if v == s:
        print(s.id)
    elif v.pi == None:
        print("no path from 's' to 'v' exsts")
    else:
        print_path(G, s, v.pi)
        print(v.id)


if __name__ == "__main__":
    V = {}
    for i in range(8):
        V[i] = Vertex(i)
    E = []
    E.append((0, 1, 1))
    E.append((0, 4, 1))
    E.append((1, 0, 1))
    E.append((1, 5, 1))
    E.append((2, 3, 1))
    E.append((2, 5, 1))
    E.append((2, 6, 1))
    E.append((3, 2, 1))
    E.append((3, 6, 1))
    E.append((3, 7, 1))
    E.append((4, 0, 1))
    E.append((5, 1, 1))
    E.append((5, 2, 1))
    E.append((5, 6, 1))
    E.append((6, 2, 1))
    E.append((6, 3, 1))
    E.append((6, 5, 1))
    E.append((6, 7, 1))
    E.append((7, 3, 1))
    E.append((7, 6, 1))

    G = MatrixGraph(V, E)
    bfs(G, V[1])
    print_path(G, V[1], V[3])

    print()

    G = AdjListGraph(V, E)
    bfs(G, V[1])
    print_path(G, V[1], V[3])
