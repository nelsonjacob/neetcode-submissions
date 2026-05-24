"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        
        if not node:
            return None
        old_to_new_map = {}


        def dfs(curr_node):
            if curr_node in old_to_new_map:
                return old_to_new_map[curr_node]
            

            node_copy = Node(curr_node.val)

            old_to_new_map[curr_node] = node_copy

            for neighbor in curr_node.neighbors:

                node_copy.neighbors.append(dfs(neighbor))

            return node_copy

        
        return dfs(node)
            