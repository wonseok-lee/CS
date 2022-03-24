# 4 6
# 101111
# 101010
# 101011
# 111011

import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())
matrix=[input().strip() for _ in range(n)]
dirs=[[1,0],[-1,0],[0,1],[0,-1]]
visited=[[0 for _ in range(m)] for _ in range(n)]

def bfs():
    queue=deque()
    queue.append((0,0))
    visited[0][0]=1
    while queue:
        x,y=queue.popleft()
        for dx,dy in dirs:
            nx=x+dx
            ny=y+dy
            if nx<0 or n<=nx or ny<0 or m<=ny:
                continue
            if matrix[nx][ny]=='0':
                continue
            if visited[nx][ny]!=0:
                continue
            visited[nx][ny]=visited[x][y]+1
            queue.append((nx,ny))

bfs()
print(visited[n-1][m-1])







