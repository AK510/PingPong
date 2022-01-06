from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.admatrix = [[0 for i in range(vertices)]for j in range(vertices)]
        self.visited = [0 for i in range(vertices)]

    def addEdge(self, u, v):
        self.admatrix[u][v] = self.admatrix[v][u] = 1
        self.graph[u].append(v)


def DepthFirstSearch(graph, s):
    print(s, end=" ")
    graph.visited[s] = 1
    for j in range(graph.V):
        if graph.admatrix[s][j] == 1 and graph.visited[j] == 0:
            DepthFirstSearch(graph, j)


g = Graph(18)
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 5)
g.addEdge(1, 6)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(3, 0)
g.addEdge(3, 1)
g.addEdge(3, 2)
g.addEdge(4, 2)
g.addEdge(4, 3)
g.addEdge(4, 6)
g.addEdge(5, 1)
g.addEdge(5, 2)
g.addEdge(6, 1)
g.addEdge(6, 4)

print("\nDepth First Search is as below :- ")
DepthFirstSearch(g, 2)
