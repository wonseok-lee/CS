import sys
from collections import deque

si=sys.stdin.readline

n,l,r=map(int,si().split())
grid=[list(map(int,si().split())) for _ in range(n)]
visited=[[False for _ in range(n)] for _ in range(n)]
group=[]
dirs=[[1,0],[-1,0],[0,1],[0,-1]]
queue=deque()
answer=0

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def go(x,y,num):
    if not in_range(x,y):
        return False

    diff=abs(grid[x][y]-num)

    # return not visited[x][y] and l<=diff and diff<=r 
    if not visited[x][y] and l<=diff and diff<=r:
        return True
    else:
        return False

def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j]=False

def bfs():
    while queue:
        x,y=queue.popleft()
        for dx,dy in dirs:
            nx,ny=x+dx,y+dy

            if go(nx,ny,grid[x][y]):
                queue.append((nx,ny))
                group.append((nx,ny))
                visited[nx][ny]=True

def merge():
    summation=sum([grid[x][y] for x,y in group])
    for x,y in group:
        grid[x][y]=summation//len(group)

def move():
    global group

    initialize_visited()
    changed=False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group=[]
                queue.append((i,j))
                group.append((i,j))
                visited[i][j]=True

                bfs()

                if len(group)>1:
                    changed=True
                
                merge()
        
    return changed

while True:
    changed=move()
    if not changed:
        break
    answer+=1

print(answer)

