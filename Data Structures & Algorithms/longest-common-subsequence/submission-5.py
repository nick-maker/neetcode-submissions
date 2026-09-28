class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
         cat
        c3210
        r2210
        a2210
        b1110
        t1110
         0000   
        text1 = crabt
        text2 = cat

        """
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for m in range(len(text1) - 1, -1, -1):
            for n in range(len(text2) - 1, -1, -1):
                if text1[m] == text2[n]:
                    dp[m][n] = 1 + dp[m+1][n+1]
                else:
                    dp[m][n] = max(dp[m+1][n], dp[m][n+1])
        
        return dp[0][0]

