class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        old_to_new = {}

        def dfs(curr):
            if curr in old_to_new:
                return old_to_new[curr]

            # Clone the node
            copy = Node(curr.val)
            old_to_new[curr] = copy

            # Clone neighbors recursively
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
