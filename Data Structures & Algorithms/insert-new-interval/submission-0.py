class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.sort()
        solution = list()
        start, end = newInterval
        n = len(intervals)

        i = 0

        while i < n and intervals[i][1] < start:
            solution.append(intervals[i])
            i += 1

        

        while i < n and intervals[i][0] <= end:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i += 1

        solution.append([start, end])

        while i < n:
            solution.append(intervals[i])
            i += 1

        return solution