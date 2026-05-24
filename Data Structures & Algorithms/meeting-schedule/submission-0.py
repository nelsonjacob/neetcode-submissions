"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:


        # some greedy approach, where we consider the start time of the first meeting to end doesn't overlap with the next meeting

        # how can we sort in python by the start times


        meetings = sorted(intervals, key=lambda x: x.start)

        last_meeting_end = 0
        for m in meetings:
            if m.start < last_meeting_end:
                return False
            last_meeting_end = m.end

        return True