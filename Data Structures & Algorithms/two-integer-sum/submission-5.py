class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int) #num, index
        for (index, num) in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], index]
            seen[num] = index
        return []
            


