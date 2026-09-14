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
                if not stack or c != pairs[stack.pop()]:
                    return False
        return not stack