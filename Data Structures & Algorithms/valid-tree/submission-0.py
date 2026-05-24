
from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # What is a tree in terms of graph theory? We know this problem is undirected. 
        # If there are n nodes, there should be n-1 edges. 


        
        if (n-1) != len(edges):
            return False


        D = defaultdict(list)

        for edge in edges:
            D[edge[0]].append(edge[1])
            D[edge[1]].append(edge[0])


        visited = set()

        queue = deque([0])
        visited.add(0)

        while queue:
            node = queue.popleft()

            for neighbor in D[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


        return len(visited) == n

    








        