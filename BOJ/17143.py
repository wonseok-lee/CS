from re import L
import sys

si=sys.stdin.readline
r, c, m = map(int,si().split())
answer=0
blank=(-1,-1,-1)

grid=[[blank for _ in range(c)] for _ in range(r)]
nxt_grid=[[blank for _ in range(c)] for _ in range(r)]

for _ in range(m):
    x,y,s,d,z=map(int,si().split())
    if d<=2:
        s%=(2*r-2)
    else:
        s%=(2*c-2)
    grid[x-1][y-1]=(z,s,d-1)


def in_range(x,y):
    return 0<=x and x<r and 0<=y and y<c

def got_shark(col):
    global answer

    for row in range(r):
        if grid[row][col]!=blank:
            shark_size,_,_=grid[row][col]

            answer+=shark_size
            grid[row][col]=blank
            break

def next_shark(x,y,dist,move_dir):
    dirs=[[-1,0],[1,0],[0,1],[0,-1]]

    for _ in range(dist):
        dx,dy=dirs[move_dir]
        nx,ny=x+dx,y+dy

        if in_range(nx,ny):
            x,y=nx,ny
        else:
            if move_dir%2==0:
                move_dir=move_dir+1
            else:
                move_dir=move_dir-1
            dx,dy=dirs[move_dir]
            x,y=x+dx,y+dy
            # x,y=x+dirs[move_dir],y+dirs[move_dir]

    return (x, y, move_dir)

def move(x,y):
    shark_size,dist,move_dir=grid[x][y]
    nx,ny,ndir=next_shark(x,y,dist,move_dir)

    n_shark=(shark_size, dist,ndir)

    if n_shark>nxt_grid[nx][ny]:
        nxt_grid[nx][ny]=n_shark


def move_all():
    for i in range(r):
        for j in range(c):
            nxt_grid[i][j]=blank

    for i in range(r):
        for j in range(c):
            if grid[i][j]!=blank:
                move(i,j)

    for i in range(r):
        for j in range(c):
            grid[i][j]=nxt_grid[i][j]

def simulate(col):
    got_shark(col)
    move_all()

for col in range(c):
    simulate(col)

print(answer)
