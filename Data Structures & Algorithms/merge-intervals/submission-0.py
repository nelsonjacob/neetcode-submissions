class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])
        solution = []


        current_interval = [intervals[0][0], intervals[0][1]]

        for start, end in intervals:
            if start <= current_interval[1]:
                current_interval[1] = max(current_interval[1], end)
            else:
                solution.append(current_interval)
                current_interval = [start,end]
                
        solution.append(current_interval)

        return solution

