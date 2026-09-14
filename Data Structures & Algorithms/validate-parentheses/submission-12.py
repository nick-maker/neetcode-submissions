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
                if stack:
                    right = pairs[stack.pop()]
                    if c != right:
                        return False
                else:
                    return False

        return not stack