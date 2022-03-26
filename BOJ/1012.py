# 2
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
# 10 10 1
# 5 5

import sys

input=sys.stdin.readline
sys.setrecursionlimit(100000)

dirs=[[1,0],[-1,0],[0,-1],[0,1]]
 
def dfs(x,y):
    visited[x][y]=True
    for dx,dy in dirs:
        nx=x+dx
        ny=y+dy
        if nx<0 or n<=nx or ny<0 or m<=ny:
            continue
        if visited[nx][ny]:
            continue
        if matrix[nx][ny]==0:
            continue
        dfs(nx,ny)

trial=int(input())
while trial:
    trial-=1
    m,n,k=map(int,input().split())
    matrix=[[0] * m for _ in range(n)]
    visited=[[False for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        y,x=map(int,input().split())
        matrix[x][y]=1
    
    answer=0
    for x in range(n):
        for y in range(m):
            if matrix[x][y]==0 or visited[x][y]:
                continue
            answer+=1
            dfs(x,y)
    print(answer)
