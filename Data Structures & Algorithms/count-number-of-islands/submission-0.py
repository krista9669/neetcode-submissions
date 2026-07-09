class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        stack = []
        visited = [[False] * cols for _ in range(rows)]
        count = 0
        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and not visited[row][col]:
                    count += 1
                    stack.append((row,col))
                    visited[row][col] = True
                    while stack:
                        curr_row,curr_col = stack.pop()
                        for r,c in directions:
                            new_row = r + curr_row
                            new_col = c + curr_col
                            if (0<=new_row<rows and
                                0<=new_col<cols and
                                not visited[new_row][new_col] and
                                grid[new_row][new_col] == '1'):
                                visited[new_row][new_col] = True
                                stack.append((new_row,new_col))
        return count