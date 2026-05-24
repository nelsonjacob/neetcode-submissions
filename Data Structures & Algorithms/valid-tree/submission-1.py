
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # What is a tree in terms of graph theory? We know this problem is undirected. 
        # If there are n nodes, there should be n-1 edges. 

        if len(edges) != (n-1): # essentially, is this a valid MST?
            return False

        

        # given any node (0), can we reach all of the other nodes through a graph traversal algorithm?

        V = defaultdict(list)

        for v1, v2 in edges:
            V[v1].append(v2)
            V[v2].append(v1)

        seen = set()

        def dfs(node):
            for neighbor in V[node]:
                if neighbor not in seen:

                    seen.add(neighbor)
                    dfs(neighbor)

        seen.add(0)
        dfs(0)


        return len(seen) == n



