class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_count = len(grid)
        col_count = len(grid[0])
        island_count = 0

        def sink_island(row, col):
            # 出界就停
            if row < 0 or row >= row_count or col < 0 or col >= col_count:
                return
            # 是水(或已經淹過)就停
            if grid[row][col] == "0":
                return

            grid[row][col] = "0"          # 淹掉這一格
            sink_island(row + 1, col)     # 往下
            sink_island(row - 1, col)     # 往上
            sink_island(row, col + 1)     # 往右
            sink_island(row, col - 1)     # 往左

        for row in range(row_count):
            for col in range(col_count):
                if grid[row][col] == "1":     # 找到新的島
                    island_count += 1
                    sink_island(row, col)     # 把整座島淹掉

        return island_count