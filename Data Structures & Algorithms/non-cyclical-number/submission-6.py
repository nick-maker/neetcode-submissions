class Solution:
    def isHappy(self, n: int) -> bool:
        # if it is 1 then return True
        seen = defaultdict(int)
        # function to determine the sum of the squares of its digits
        def cycle(output) -> int:
            res = 0
            while output > 0:
                digits = output % 10
                res += digits ** 2
                output //= 10
            
            if res == 1:
                return True
            if res in seen:
                return False
            seen[res] += 1
            return cycle(res)
        
        return cycle(n)
