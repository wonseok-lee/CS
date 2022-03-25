# 3 6
# D...*.
# .X.X..
# ....S.

from re import L
import sys
from collections import deque

input=sys.stdin.readline
r,c=list(map(int, input().split()))

matrix=[list(input().strip()) for _ in range(r)]
dirs=[[-1,0],[1,0],[0,1],[0,-1]]
visited=[[False for _ in range(c)] for _ in range(r)]
dist_water=[[-1 for _ in range(c)] for _ in range(r)]
dist_dog=[[-1 for _ in range(c)] for _ in range(r)]

# goal,rock,water,start=[],[],[],[]

# for i in range(r):
#     for j in range(c):
#         if matrix[i][j]=='*':
#             water.append((i,j))
#         elif matrix[i][j]=='X':
#             rock.append((i,j))
#         elif matrix[i][j]=='D':
#             goal.append((i,j))
#         elif matrix[i][j]=='S':
#             start.append((i,j))

def water_fill():
    q=deque()
    for i in range(r):
        for j in range(c):
            if matrix[i][j]=='*':
                q.append((i,j))
                visited[i][j]=True
                dist_water[i][j]=0
    while q:
        x,y=q.popleft()
        for dx,dy in dirs:
            nx=x+dx
            ny=y+dy
            if nx<0 or r<=nx or ny<0 or c<=ny:
                continue
            if visited[nx][ny]:
                continue
            if matrix[nx][ny]!='.':
                continue
            q.append((nx,ny))
            visited[nx][ny]=True
            dist_water[nx][ny]=dist_water[x][y]+1

def bfs_dog():
    q=deque()
    for i in range(r):
        for j in range(c):
            visited[i][j]=False
            if matrix[i][j]=='S':
                q.append((i,j))
                visited[i][j]=True
                dist_dog[i][j]=0
    while q:
        x,y=q.popleft()
        for dx,dy in dirs:
            nx=x+dx
            ny=y+dy
            if nx<0 or r<=nx or ny<0 or c<=ny:
                continue
            if visited[nx][ny]:
                continue
            if matrix[nx][ny]!='.' and matrix[nx][ny]!='D':
                continue
            if dist_water[nx][ny]!=-1 and dist_water[nx][ny]<=dist_dog[x][y]+1:
                continue
            q.append((nx,ny))
            visited[nx][ny]=True
            dist_dog[nx][ny]=dist_dog[x][y]+1

water_fill()
bfs_dog()
for i in range(r):
    for j in range(c):
        if matrix[i][j]=='D':
            if dist_dog[i][j]==-1:
                print('KAKTUS')
            else:
                print(dist_dog[i][j])