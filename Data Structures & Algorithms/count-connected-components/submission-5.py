
from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        component_count = 0

        # what is a good way to map the edges, maybe some adjacency list?
        # for any node n: what are it's neighbors


        D = defaultdict(list)

        for edge in edges:
            D[edge[0]].append(edge[1])
            D[edge[1]].append(edge[0])

        visited = set()

        for node in range(n):


            if node in visited:
                continue
            

            component_count += 1
            queue = deque([node])
            visited.add(node)

            while queue:
                curr_node = queue.popleft()

                for neighbor in D[curr_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

            






        return component_count




