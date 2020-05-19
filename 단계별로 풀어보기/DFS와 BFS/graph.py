import heapq


class Graph():
    graph = {}

    def __init__(self):
        self.graph = {}

    def set_graph(self, p, c):
        if p in self.graph.keys():
            child = self.graph[p]
            heapq.heappush(child, c)
            self.graph[p] = child
        else:
            self.graph[p] = [c]

        if c in self.graph.keys():
            child = self.graph[c]
            heapq.heappush(child, p)
            self.graph[c] = child
        else:
            self.graph[c] = [p]

    def get_graph(self):
        return self.graph

