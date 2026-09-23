class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        [1, 1, 3, 3]
        [1, 1, 4, 0]

        [2,9,8,3,6]
        [2,9,10,12,16]
        """
        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            pick = (dp[i-2] if i > 1 else 0) + num
            nopick = dp[i-1] if i > 0 else 0
            dp[i] = max(pick, nopick)
        
        return dp[-1]

        
