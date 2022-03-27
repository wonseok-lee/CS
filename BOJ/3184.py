# 9 12
# .###.#####..
# #.oo#...#v#.
# #..o#.#.#.#.
# #..##o#...#.
# #.#v#o###.#.
# #..#v#....#.
# #...v#v####.
# .####.#vv.o#
# .......####.

import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
r,c=map(int,input().split())

matrix=[list(map(str, input().strip())) for _ in range(r)]
dirs=[[1,0],[-1,0],[0,1],[0,-1]]
visited=[[False for _ in range(c)] for _ in range(r)]

total_wolf,total_sheep=0,0
sheep,wolf=0,0

def dfs(x,y):
    visited[x][y]=True
    global wolf, sheep
    if matrix[x][y]=='o':
        sheep+=1
    if matrix[x][y]=='v':
        wolf+=1
    
    for dx,dy in dirs:
        nx,ny=x+dx,y+dy
        if nx<0 or r<=nx or ny<0 or c<=ny:
            continue
        if visited[nx][ny]:
            continue
        if matrix[nx][ny]=='#':
            continue
        dfs(nx,ny)
        
    

for x in range(r):
    for y in range(c):
        
        if matrix[x][y]=='#' or visited[x][y]:
            continue
        else:
            sheep,wolf=0,0
            dfs(x,y)
            if wolf>=sheep:
                total_wolf+=wolf
            else:
                total_sheep+=sheep

sys.stdout.write(str(total_sheep)+' '+ str(total_wolf))
