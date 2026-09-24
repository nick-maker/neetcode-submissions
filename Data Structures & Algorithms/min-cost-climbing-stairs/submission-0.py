class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        1, 2, 3
        1, 2, 4
        """

        dp = [0] * len(cost)

        for i in range(len(cost)):
            dp[0] = cost[0]
            dp[1] = cost[1]
            if i > 1:
                dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
        
        return min(dp[-1], dp[-2])