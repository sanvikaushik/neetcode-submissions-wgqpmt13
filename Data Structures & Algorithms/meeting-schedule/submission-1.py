"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        if len(intervals) <= 1:
            return True

        # make a start list
        start = []
        end = []
        intervals.sort(key=lambda x: x.start)

        for i in intervals:

            start.append(i.start)
            end.append(i.end)

        l = 1
        r = 0
        
        while l < len(start):
            if start[l] < end[r]:
                return False
            l += 1
            r += 1
        return True
    