class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} # value, index
        for index, num in enumerate(nums):
            indices[num] = index
        
        for index, num in enumerate(nums):
            find = target - num
            if find in indices and indices[find] != index:
                return [index, indices[find]]
        
        return []

