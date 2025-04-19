from collections import defaultdict
import heapq

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)

        # Build the graph using a min-heap to maintain lexical order
        for src, dest in tickets:
            heapq.heappush(graph[src], dest)

        result = []

        def dfs(airport):
            while graph[airport]:
                next_dest = heapq.heappop(graph[airport])
                dfs(next_dest)
            result.append(airport)

        # Start from JFK
        dfs("JFK")

        # Reverse the path because we append after visiting all neighbors
        return result[::-1]
