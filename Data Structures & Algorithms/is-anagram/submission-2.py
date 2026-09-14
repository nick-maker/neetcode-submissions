class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        for c in s:
            if c in dictS:
                dictS[c] += 1
            else:
                dictS[c] = 1
        
        for c in t:
            if c in dictT:
                dictT[c] += 1
            else:
                dictT[c] = 1
        
        return dictS == dictT