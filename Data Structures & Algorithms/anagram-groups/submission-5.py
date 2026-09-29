class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for string in strs:
            sortedstr = "".join(sorted(string)) #sorted will return array
            seen[sortedstr].append(string)
        
        return list(seen.values())

