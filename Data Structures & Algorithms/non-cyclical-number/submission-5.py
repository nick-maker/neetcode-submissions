class Solution:
    def isHappy(self, n: int) -> bool:
        
        def next_num(x):
            total = 0
            while x > 0:
                total += (x % 10) ** 2
                x //= 10
            return total
        
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = next_num(n)
        
        return True
       