class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        def helper(m: int) -> Bool:
            output = 0
            while m > 0:
                digit = m % 10
                digit = digit ** 2
                output += digit
                m = m // 10
            print(output)
            if output in seen:
                return False
            seen.add(output)
            
            if output == 1:
                return True
            else:
                return helper(output)

        return helper(n)