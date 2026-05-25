class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        seen = set() #(tuple)
        ans = 0

        def bfs(r, c):
            q = collections.deque()
            seen.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in directions:
                    new_r = row + dr
                    new_c = col + dc
                    if (new_r in range(rows) and
                        new_c in range(cols) and 
                        grid[new_r][new_c] == "1" and 
                        (new_r, new_c) not in seen):
                            seen.add((new_r, new_c))
                            q.append((new_r, new_c))

    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    ans += 1
                    bfs(r, c)

        return ans