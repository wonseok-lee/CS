# 실패
from re import L
import sys
from collections import deque

si=sys.stdin.readline
N=int(si())
grid=[list(map(int,si().split())) for _ in range(N)]

start_x,start_y=-1,-1
for i in range(N):
    for j in range(N):
        if grid[i][j]==9:
            start_x,start_y=i,j
            grid[i][j]=0

visited=[[False for _ in range(N)] for _ in range(N)]
step=[[0 for _ in range(N)] for _ in range(N)]
dirs=[[0,1],[1,0],[0,-1],[-1,0]]

time=0
ate=0
shark_init=2

def initialize_visited():
    for i in range(N):
        for j in range(N):
            visited[i][j]=False

def bfs():
    global shark_init,ate,time
    global start_x,start_y

    initialize_visited()

    queue=deque()
    queue.append((start_x,start_y))

    visited[start_x][start_y]=True
    step[start_x][start_y]=0

    while queue:
        x,y=queue.popleft()

        for dx,dy in dirs:
            nx,ny=x+dx,y+dy
            if nx<0 or N<=nx or ny<0 or N<=ny:
                continue
            if visited[nx][ny]:
                continue
            if grid[nx][ny]>shark_init:
                continue
            queue.append((nx,ny))
            visited[nx][ny]=True
            step[nx][ny]=step[x][y]+1
    
    queue_new=deque()
    queue_new.append((-1,-1))
    for i in range(N):
        for j in range(N):
            if not visited[i][j] or grid[i][j]==shark_init or not grid[i][j]:
                continue
            queue_new.append((i,j))
    
    queue_new=deque(sorted(queue_new))
    new_x,new_y=queue_new.popleft()
    if new_x!=-1 and new_y!=-1:
        time+=step[new_x][new_y]
        grid[new_x][new_y]=0
        start_x,start_y=new_x,new_y
        ate+=1

        if ate==shark_init:
            ate=0
            shark_init+=1
        
        return True
    else:
        return False

while True:
    bfs_res=bfs()
    if not bfs_res:
        break

print(time)
