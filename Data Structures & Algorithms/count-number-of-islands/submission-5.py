class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        island_count = 0

        def bfs(i, j):
            grid[i][j] = "0"
            stack = [(i, j)]

            while stack:
                row, col = stack.pop()

                for next_row, next_col in [(row + 1, col), (row - 1, col),
                                           (row, col + 1), (row, col - 1)]:
                    is_inside = 0 <= next_row < m and 0 <= next_col < n
                    if is_inside and grid[next_row][next_col] == "1":
                        grid[next_row][next_col] = "0"
                        stack.append((next_row, next_col))

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":                
                    island_count += 1
                    bfs(row, col)                

        return island_count