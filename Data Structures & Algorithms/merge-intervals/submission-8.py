class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [1,7], [2,3], [3,6]

        """
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]
        for start, end in intervals:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        
        return output
                

