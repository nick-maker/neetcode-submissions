class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [1,7], [2,3], [3,6]

        """
        intervals.sort()
        output = []
        for start, end in intervals:
            if output and start <= output[-1][1]:
                    output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])
        
        return output
                

