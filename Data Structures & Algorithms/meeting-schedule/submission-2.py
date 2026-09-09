"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:


        intervals.sort(key=lambda i: i.end)

        max_end = float('-inf')

        for interval in intervals:
            if interval.start < max_end:
                return False
            
            max_end = interval.end

        return True


