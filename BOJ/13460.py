# 10 10
# ##########
# #R#...#..#
# #...#....#
# #######.##
# #....#..##
# #.####O#B#
# #.#......#
# #........#
# #....#...#
# ##########

import sys
from collections import deque

si=sys.stdin.readline

n,m=map(int,si().split())

matrix=[list(map(str,si().strip())) for _ in range(n)]
dirs=[[1,0],[-1,0],[0,-1],[0,1]]
visited={}

for i in range(n):
    for j in range(m):
        if matrix[i][j]=='B':
            matrix[i][j]=='.'
            blue=(i,j)
        elif matrix[i][j]=='R':
            matrix[i][j]=='.'
            red=(i,j)

def move(x,y,dx,dy):
    move=0
    while matrix[x+dx][y+dy]!='#':
        if matrix[x+dx][y+dy]=='O':
            return 0,0,0
        x+=dx
        y+=dy
        move+=1
    return x,y,move

def simulation():
    rx,ry=red[0],red[1]
    bx,by=blue[0],blue[1]
    queue=deque()
    visited[rx,ry,bx,by]=0
    queue.append((rx,ry,bx,by))
    while queue:
        rx,ry,bx,by=queue.popleft()
        for dx,dy in dirs:
            nrx,nry,rmove=move(rx,ry,dx,dy)
            nbx,nby,bmove=move(bx,by,dx,dy)

            if nbx==0 and nby==0:
                continue
            elif nrx==0 and nry==0:
                if visited[rx,ry,bx,by]>=10:
                    print(-1)
                else:
                    print(visited[rx,ry,bx,by]+1)
                return
            elif nrx==nbx and nry==nby:
                if rmove>bmove:
                    nrx-=dx
                    nry-=dy
                else:
                    nbx-=dx
                    nby-=dy
            
            if (nrx,nry,nbx,nby) not in visited:
                visited[nrx,nry,nbx,nby]=visited[rx,ry,bx,by]+1
                queue.append((nrx,nry,nbx,nby))
        
        if not queue or visited[rx,ry,bx,by]>10:
            print(-1)
            return

simulation()
            