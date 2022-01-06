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


def BreadthFirstSearch(graph, s):
    queue = []
    queue.append(s)
    graph.visited[s] = 1

    while queue:

        s = queue.pop(0)
        print(s, end=" ")

        for i in range(graph.V):
            if graph.admatrix[s][i] and graph.visited[i] == False:
                queue.append(i)
                graph.visited[i] = True


g = Graph(7)
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

print("\nBreadth First Traversal is as below :- ")
BreadthFirstSearch(g, 2)
