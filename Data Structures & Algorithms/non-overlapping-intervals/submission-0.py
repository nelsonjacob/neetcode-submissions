class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        


        intervals.sort(key = lambda x: x[1])
        

        non_overlapping_count = 0

        max_ending_time = float('-inf')

        for start, end in intervals:
            if start >= max_ending_time:
                non_overlapping_count += 1
                max_ending_time = end
            
        return len(intervals) - non_overlapping_count


