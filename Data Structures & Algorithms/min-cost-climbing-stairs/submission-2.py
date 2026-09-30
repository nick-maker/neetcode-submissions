class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        1212111
        1224344
        """
        dp = [0] * len(cost)

        for i,c in enumerate(cost):
            prev1 = dp[i - 1] if i > 0 else 0
            prev2 = dp[i - 2] if i > 1 else 0
            dp[i] = cost[i] + min(prev1, prev2)
        
        return min(dp[-1], dp[-2])
