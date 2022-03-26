# 1 1
# 0
# 2 2
# 0 1
# 1 0
# 3 2
# 1 1 1
# 1 1 1
# 5 4
# 1 0 1 0 0
# 1 0 0 0 0
# 1 0 1 0 1
# 1 0 0 1 0
# 5 4
# 1 1 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 1 1 1
# 5 5
# 1 0 1 0 1
# 0 0 0 0 0
# 1 0 1 0 1
# 0 0 0 0 0
# 1 0 1 0 1
# 0 0

import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

def dfs(x,y):
    visited[x][y]=True
    for dx,dy in dirs:
        nx,ny=x+dx,y+dy
        if nx<0 or h<=nx or ny<0 or w<=ny:
            continue
        if visited[nx][ny]:
            continue
        if matrix[nx][ny]==0:
            continue
        dfs(nx,ny)

dirs=[[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[1,-1],[1,1],[-1,1]]

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break

    matrix =[list(map(int, input().split())) for _ in range(h)]
    visited=[[False for _ in range(w)] for _ in range(h)]
    
    answer=0

    for x in range(h):
        for y in range(w):
            if matrix[x][y]==0 or visited[x][y]:
                continue
            answer+=1
            dfs(x,y)
            
    print(answer)
    




