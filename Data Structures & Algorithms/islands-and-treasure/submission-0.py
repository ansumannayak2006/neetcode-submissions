class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append([r,c])
                    visited.add((r,c))

        def addn(r,c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c]==-1 or (r,c) in visited):
                return
            q.append([r,c])
            visited.add((r,c))

        dist = 0
        while q:
            
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c]=dist
                addn(r+1,c)
                addn(r-1,c)
                addn(r,c+1)
                addn(r,c-1)         
            dist+=1

