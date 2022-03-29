import sys
from collections import deque

input=sys.stdin.readline
m,n,h=map(int,input().split())
dirs=[[1,0,0],[-1,0,0], \
      [0,1,0],[0,-1,0], \
      [0,0,1],[0,0,-1]]

graph=[[] for _ in range(h)]
ripe=[]
wall=[]
for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int,input().split())))
        for k in range(m):
            if graph[i][j][k]==1:
                ripe.append((j,k,i))

visited=[[[-1 for _ in range(m)] for _ in range(n)] for _ in range(h)]

def bfs(ripe):
    queue=deque()
    for elt in ripe:
        queue.append(elt)
        a,b,c=elt
        visited[c][a][b]=1
    while queue:
        x,y,z=queue.popleft()
        for dx,dy,dz in dirs:
            nx,ny,nz=x+dx,y+dy,z+dz
            if nx<0 or ny<0 or nz<0 or\
                n<=nx or m<=ny or h<=nz:
                continue
            if visited[nz][nx][ny]!=-1:
                continue
            if graph[nz][nx][ny]!=0:
                continue
            
            visited[nz][nx][ny]=visited[z][x][y]+1
            queue.append((nx,ny,nz))

bfs(ripe)
answer=0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j]==-1:
                continue
            if visited[k][i][j]==-1:
                answer=-1
            if answer==-1:
                continue
            answer=max(answer,visited[k][i][j])

if answer==-1:
    print(answer)
else:
    print(answer-1)
