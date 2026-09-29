class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        s = XYYX, k = 2
        x:2, y:2
        """
        count = Counter()
        l = 0
        res = 0
        maxf = 0
        for i, c in enumerate(s):
            count[c] += 1
            maxf = max(maxf, count[c])
            while (i - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        return res




