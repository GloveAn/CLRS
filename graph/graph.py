#!/usr/bin/python
from collections import deque
from operator import attrgetter
import sys
sys.path.append("../data_structures")
import heap


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


    def edges(self):
        raise NotImplementedError


    def neighbors(self, u):
        raise NotImplementedError


    def weight(self, u, v):
        raise NotImplementedError


# chapter 22.1
class MatrixGraph(Graph):
    def __init__(self, V, E):
        super().__init__(V, E)

        n = len(V)

        self._matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i, j, w in E:
            self._matrix[i][j] = w


    def edges(self):
        e = []
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix)):
                if self._matrix[i][j]:
                    e.append((i, j, self._matrix[i][j]))
        return e


    def neighbors(self, u):
        u = u.id
        r = []

        for i in range(len(self._matrix)):
            if self._matrix[u][i]:
                r.append(self._vertices[i])

        return r


    def weight(self, u, v):
        return self._matrix[u.id][v.id]


# chapter 22.1
class AdjListGraph(Graph):
    def __init__(self, V, E):
        super().__init__(V, E)

        n = len(V)

        self._vertices = V
        self._adj_list = [[] for i in range(n)]
        for i, j, w in E:
            self._adj_list[i].append((j, w))


    def edges(self):
        e = []
        for i in range(len(self._adj_list)):
            for j, w in self._adj_list[i]:
                e.append((i, j, w))
        return e


    def neighbors(self, u):
        u = u.id
        r = []

        for i, w in self._adj_list[u]:
            r.append(self._vertices[i])

        return r


    def weight(self, u, v):
        for j, w in self._adj_list[u.id]:
            if j == v.id:
                return w


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


# chapter 24
def initialize_single_source(G, s):
    INFINITE = 0x7FFFFFFF

    for v in G.vertices():
        v.d = INFINITE
        v.pi = None
    s.d = 0


# chapter 24
def relax(u, v, w):
    if v.d > u.d + w:
        v.d = u.d + w
        v.pi = u


# chapter 24.1
def bellman_ford(G, s):
    initialize_single_source(G, s)
    for i in range(len(G.vertices()) - 1):
        for u, v, w in G.edges():
            relax(u, v, w)
    for u, v, w in G.edges():
        if v.d > u.d + w:
            return False
    return True


# chapter 24.2
def dag_shortest_paths(G, s):
    vertices = topologocal_sort(G)
    initialize_single_source(G, s)
    for u in vertices:
        for v in G.neighbors(u):
            relax(u, v, G.weight(u, v))


# chaper 24.3
def dijkstra(G, s):
    initialize_single_source(G, s)
    S = set()
    Q = heap.MinHeap(G.vertices())
    while len(Q):
        u = Q.extract_min()
        S.add(u)
        for v in G.neighbors(u):
            relax(u, v, G.weight(u, v))  # decrease_key!!


# chapter 25
def print_all_pairs_shortest_path(PI, i, j):
    if i == j:
        print(i.id)
    elif PI[i][j] == None:
        print("no path from 'i' to 'j' exists")
    else:
        print_all_pairs_shortest_path(PI, i, PI[i][j])
        print(j.id)


# chapter 25.1
def extend_shortest_paths(G):
    INFINITE = 0x7FFFFFFF

    vertices = G.vertices()
    n = len(vertices)
    L_prime = [[INFINITE for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                L_prime = min(L_prime, \
                    L[i][k] + G.weight(vertices[k], vertices[j]))

    return L_prime


def show_all_pairs_shortest_paths(G):
    pass


def floyd_warshall(G):
    vertices = G.vertices()

    n = len(vertices)
    D1 = [[G.weight(vertices[i], vertices[j]) for j in range(n)] for i in range(n)]
    D2 = [[G.weight(vertices[i], vertices[j]) for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                D2[i][j] = min(D1[i][j], D1[i][k] + D1[k][j])

        D1, D2 = D2, D1

    return D1


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
