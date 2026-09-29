class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def next_num(x):
            total = 0
            while x > 0:
                x, d = divmod(x, 10)
                total += d * d
            return total

        def check(x) -> bool:
            if x == 1:                  # 1. 檢查目前這個數
                return True
            if x in seen:
                return False
            seen.add(x)                 # 2. 記錄
            return check(next_num(x))   # 3. 再走下一步

        return check(n)
