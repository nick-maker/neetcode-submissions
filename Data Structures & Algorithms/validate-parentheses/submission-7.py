class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "[": "]", "{": "}"}
        
        for c in s:
            if c in pairs:  
                # 是左括號 → 直接進 stack,「記住等等要配對誰」
                stack.append(c)
            else:  
                # 是右括號 → 檢查 stack 頂端的左括號能不能配對
                if not stack or pairs[stack.pop()] != c:
                    return False
        
        return not stack