class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        ctMax = 0

        def bfs(r,c):
            ctTemp = 1
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            ctTemp = 1
            while q:
                row, col = q.popleft()
                for dr,dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c]==1 and (r,c) not in visited:
                        ctTemp+=1
                        q.append((r,c))
                        visited.add((r,c))
            return ctTemp


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area1 = bfs(r,c)
                    if area1 > ctMax:
                        ctMax = area1
        return ctMax
        