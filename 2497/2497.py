import heapq
from collections import defaultdict

class Solution(object):
    def maxStarSum(self, vals, edges, k):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(vals)
        graph = defaultdict(list)

        # Build undirected graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        max_sum = float('-inf')

        for center in range(n):
            neighbors = graph[center]

            # Get neighbor values
            neighbor_vals = [vals[nei] for nei in neighbors if vals[nei] > 0]

            # Pick top k positive neighbors (or less)
            top_k = heapq.nlargest(k, neighbor_vals)

            star_sum = vals[center] + sum(top_k)
            max_sum = max(max_sum, star_sum)

        return max_sum
