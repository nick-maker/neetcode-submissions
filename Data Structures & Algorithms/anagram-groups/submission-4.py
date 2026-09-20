class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            sortedString = "".join(sorted(s))
            seen[sortedString].append(s)
        
        return [value for value in seen.values()]

    
    """
    ["act","pots","tops","cat","stop","hat"]
    ["act", "stop", "stop", "act", "stop", "aht"]
    """
