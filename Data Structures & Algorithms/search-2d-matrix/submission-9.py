class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            """
            [[1,2,4,8]
            [10,11,12,13]
            [14,20,30,40]]
            """
            top, bottom = 0, len(matrix) - 1
            left, right = 0, len(matrix[0]) - 1
            while top <= bottom:
                mid = (top + bottom) // 2
                if matrix[mid][0] == target:
                    return True
                elif matrix[mid][0] < target:
                    top = mid + 1
                elif matrix[mid][0] > target:
                    bottom = mid - 1
            row = bottom
            while left <= right:
                mid = (left + right) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False


