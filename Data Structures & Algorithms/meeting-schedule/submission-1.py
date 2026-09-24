"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        lastEnd = 0
        for interval in intervals:
            start = interval.start
            end = interval.end
            if start < lastEnd:
                return False
            lastEnd = end
        
        return True

        """
        intervals = [(5,8),(9,15)]
        lastEnd = 8
        9 > 8
        lastEnd = 15
        return True

        intervals = [(0,30),(5,10),(15,20)]
        lastEnd = 30
        5 < 30:
        return False
        """