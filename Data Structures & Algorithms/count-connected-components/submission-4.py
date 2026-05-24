
from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        node_neighbor_map = defaultdict(list)

        for edge in edges:
            node_neighbor_map[edge[0]].append(edge[1])
            node_neighbor_map[edge[1]].append(edge[0])

        visited = set()

        tree_count = 0

        for node in range(n):
            if node in visited:
                continue

            # else, let's visit this node and all neighboring nodes (BFS algo)

            queue = deque([node])

            tree_count += 1

            visited.add(node)

            while queue:
                queue_node = queue.popleft()

                visited.add(queue_node)


                for neighbor in node_neighbor_map[queue_node]:
                    
                    if neighbor not in visited:
                        visited.add(queue_node)
                        queue.append(neighbor)
            


        return tree_count