import heapq
from collections import defaultdict

class Graph(object):

    def __init__(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        """
        self.n = n
        self.adj = defaultdict(list)
        for u, v, cost in edges:
            self.adj[u].append((v, cost))

    def addEdge(self, edge):
        """
        :type edge: List[int]
        :rtype: None
        """
        u, v, cost = edge
        self.adj[u].append((v, cost))

    def shortestPath(self, node1, node2):
        """
        :type node1: int
        :type node2: int
        :rtype: int
        """
        # Dijkstra's algorithm
        dist = [float('inf')] * self.n
        dist[node1] = 0
        min_heap = [(0, node1)]  # (cost, node)

        while min_heap:
            curr_cost, u = heapq.heappop(min_heap)

            if u == node2:
                return curr_cost

            if curr_cost > dist[u]:
                continue

            for v, weight in self.adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(min_heap, (dist[v], v))

        return -1
