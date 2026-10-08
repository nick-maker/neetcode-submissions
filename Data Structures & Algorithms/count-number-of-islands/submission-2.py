class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_count = len(grid)
        col_count = len(grid[0])
        island_count = 0

        def sink_island(row, col):
            grid[row][col] = "0"
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()
                for nr, nc in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
                    if 0 <= nr < row_count and 0 <= nc < col_count and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        stack.append((nr, nc))


        for row in range(row_count):
            for col in range(col_count):
                if grid[row][col] == "1":     # 找到新的島
                    island_count += 1
                    sink_island(row, col)     # 把整座島淹掉

        return island_count