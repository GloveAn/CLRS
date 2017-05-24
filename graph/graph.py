#!/usr/bin/python
from collections import deque
from operator import attrgetter


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


# chapter 22.1
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


# chapter 22.1
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


# chapter 22.2
def print_path(G, s, v):
    if v == s:
        print(s.id)
    elif v.pi == None:
        print("no path from 's' to 'v' exsts")
    else:
        print_path(G, s, v.pi)
        print(v.id)


# chapter 22.3, exerceises 22.3-4
# errata: if line 8 of DFS-VISIT was removed.
def dfs(G):
    def dfs_visit(G, u):
        nonlocal time

        time = time + 1
        u.d = time
        u.color = GRAY
        for v in G.neighbors(u):
            if v.color == WHITE:
                v.pi = u
                dfs_visit(G, v)
        # u.color = BLACK
        time = time + 1
        u.f = time


    WHITE = 0
    GRAY = 1
    # BLACK = 2

    for u in G.vertices():
        u.color = WHITE
        u.pi = None
    time = 0
    for u in G.vertices():
        if u.color == WHITE:
            dfs_visit(G, u)


# exerceises 22.3-7
def dfs_stack(G):
    def dfs_visit_stack(G, u):
        stack = [u]
        time = 0

        while len(stack):
            time = time + 1

            u = stack.pop()
            if u.color == WHITE:
                u.color = GRAY
                u.d = time
                stack.append(u)
                for v in G.neighbors(u):
                    if v.color == WHITE:
                        stack.append(v)
            else:
                u.f = time


    WHITE = 0
    GRAY = 1

    for u in G.vertices():
        u.color = WHITE
        u.pi = None
    time = 0
    for u in G.vertices():
        if u.color == WHITE:
            dfs_visit_stack(G, u)


# chapter 22.4
def topologocal_sort(G):
    dfs(G)
    vertices = G.vertices()
    vertices.sort(key=attrgetter('f'), reverse=True)
    return vertices


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

    print()

    V = {}
    for i in range(8):
        V[i] = Vertex(i)
    E = []
    E.append((0, 1, 1))
    E.append((0, 3, 1))
    E.append((1, 4, 1))
    E.append((2, 4, 1))
    E.append((2, 5, 1))
    E.append((3, 1, 1))
    E.append((4, 3, 1))
    E.append((5, 5, 1))

    G = MatrixGraph(V, E)
    dfs(G)

    G = AdjListGraph(V, E)
    dfs_stack(G)

    vertices = topologocal_sort(G)
    print(vertices)
