# 실패
import sys
from collections import deque

si=sys.stdin.readline
N=int(si())
grid=[list(map(int,si().split())) for _ in range(N)]

visited=[[False for _ in range(N)] for _ in range(N)]
step=[[0 for _ in range(N)] for _ in range(N)]
dirs=[[0,1],[1,0],[0,-1],[-1,0]]
answer=0
time=0
ate=False

def bfs(x,y):
    global answer, ate, time,visited
    shark_init=2
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True
    eat=0

    while queue:
        food=deque(sorted(queue))
        food_num=len(food)

        for _ in range(food_num):
            x,y=queue.popleft()
            if grid[x][y]!=0 and grid[x][y]<shark_init:
                grid[x][y]=0
                eat+=1

                if eat==shark_init:
                    shark_init+=1
                    eat=0
            
                queue=deque()
                visited=[[False for _ in range(N)] for _ in range(N)]
                visited[x][y]=True
                ate=True
                answer=time

            for dx,dy in dirs:
                nx,ny=x+dx,y+dy

                if nx>=0 and N>nx and ny>=0 and N>ny and not visited[nx][ny]:
                    if grid[nx][ny]<=shark_init:
                    
                        queue.append((nx,ny))
                        visited[nx][ny]=True

                # if nx<0 or N<=nx or ny<0 or N<=ny:
                #     continue
                # if visited[nx][ny]:
                #     continue
                # if grid[nx][ny]<=shark_init:
                    
                #     queue.append((nx,ny))
                #     visited[nx][ny]=True
            if ate:
                ate=False
                break

        time+=1
    return answer


a, b = None, None
for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            a, b = i, j
            grid[i][j] = 0

print(bfs(a,b))
