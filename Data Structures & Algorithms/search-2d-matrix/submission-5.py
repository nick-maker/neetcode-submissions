class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom:
            row = top + (bottom - top) // 2
            if matrix[row][0] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bottom = row - 1
            else:
                return True
        
        row = bottom

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True
        
        return False
        """
        [1,2,4,8]
        [10,11,12,13]
        [14,20,30,40]
        target 11
        top 0 bottom 2 row 1
        top =2, bottom 2, row 2
        bottom = 1
        top = 2
        """
            
