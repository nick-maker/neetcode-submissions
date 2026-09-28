class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtracking(start):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                choice = s[start:end]
                if choice == choice[::-1]:
                    path.append(choice)
                    backtracking(end)
                    path.pop()
        
        backtracking(0)
        return res

        