class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        nums [0,3,1,3,2,3]
        dp   [0,0,0,0,0,0]
             [1,2,2,3,3,4]
        """
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                
        return max(dp)
            

        """
        nums = [1,3,6,7,9,4,10,5,6]
        output = 6
        dp =   [1,2,3,4,5,3,6,4,5]
        """
