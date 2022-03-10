import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    check[x][y] = True
    for dx, dy in (-1,0), (1,0), (0,1), (0,-1):
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = -1
                dfs(nx, ny)

def solve():
    ans = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] and not check[i][j]:
                dfs(i, j)
                ans += 1
    print(ans)

iteration = int(input())
for _ in range(iteration):
    m, n, k = map(int, input().strip().split())
    matrix = [[0]*m for _ in range(n)]
    check = [[False]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    solve()
