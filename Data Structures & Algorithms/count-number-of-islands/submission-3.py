class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        island_count = 0

        def sink_island(start_row, start_col):
            grid[start_row][start_col] = "0"
            stack = [(start_row, start_col)]

            while stack:
                row, col = stack.pop()

                # 上下左右四個鄰居
                for next_row, next_col in [(row + 1, col), (row - 1, col),
                                           (row, col + 1), (row, col - 1)]:
                    is_inside = 0 <= next_row < m and 0 <= next_col < n
                    if is_inside and grid[next_row][next_col] == "1":
                        grid[next_row][next_col] = "0"    # 放進 stack 時就淹掉
                        stack.append((next_row, next_col))

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":                 # 找到新的島
                    island_count += 1
                    sink_island(row, col)                 # 把整座島淹掉

        return island_count