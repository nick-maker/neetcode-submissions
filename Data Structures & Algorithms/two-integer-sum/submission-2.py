class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) - 1
        for i in range(n):
            for j in range(i+1, n+1):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []