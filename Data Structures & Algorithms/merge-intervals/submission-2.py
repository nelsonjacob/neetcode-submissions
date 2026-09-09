class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        intervals.sort()
        solution = list()


    


        hold_start, hold_end = intervals[0]

        for start, end in intervals:

            if start <= hold_end:

                hold_start = min(start, hold_start)
                hold_end = max(end, hold_end)

            else:
                solution.append([hold_start, hold_end])
                hold_start = start
                hold_end = end
        
        solution.append([hold_start, hold_end])

        return solution




