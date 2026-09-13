class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) < 2:
            return False
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if stack:
                    l = stack.pop()
                    if l == '(' and c == ')':
                        continue
                    elif l == '[' and c ==']':
                        continue
                    elif l == '{' and c == '}':
                        continue
                    else:
                        return False
                else:
                    return False
        return stack == []