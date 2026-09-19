class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { "(" : ")", "{" : "}", "[" : "]" }

        for c in s:
            # if left
            if c in pairs:
                stack.append(c)
            else:
            # if right
                if not stack:
                    return False
                if c != pairs[stack.pop()]:
                    return False
        return True if not stack else False