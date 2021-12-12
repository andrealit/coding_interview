# Question:
# Given employees and their schedules find the common free time.
# Table:
# Emp_ID Start_time End_Time
# 1 1 2
# 1 4 5
# 2 3 6
# 3 1 3

class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end

class Solution(object):
    def employeeFreeTime(self, schedule):
        intervals = sum(schedule, [])
        intervals.sort(key=lambda x: x.start)
        n = len(intervals)

        output = []
        last = intervals[0]
        
        for i in range[1, n]:
            curr = intervals[i]
            if curr.start < last.end:
                last = Interval(last.start, max(last.end, curr.end))
            else:
                output.append(Interval(last.end, curr.start))
                last = curr
        return output


