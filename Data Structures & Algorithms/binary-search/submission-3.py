class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1

    """
    [-1,0,2,4,6,8]
    0, 6
    mid = 3
    4 > 3
    left = mid + 1
    left = 4
    mid = 5
    left = 6


    """
    