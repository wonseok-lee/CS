import sys

si=sys.stdin.readline
r,c,t=map(int,si().split())

grid=[list(map(int,si().split())) for _ in range(r)]
grid_spread=[[0 for _ in range(c)] for _ in range(r)]
cleaner=-1

def spread(x,y):
    dirs=[[0,1],[0,-1],[1,0],[-1,0]]
    curr_dust=grid[x][y]
    for dx,dy in dirs:
        nx,ny=x+dx,y+dy
        if can_spread(nx,ny):
            grid_spread[nx][ny]+=curr_dust//5
            grid[x][y]-=curr_dust//5

def can_spread(x,y):
    return in_range(x,y) and grid[x][y]!=cleaner

def in_range(x,y):
    return 0<=x and x<r and 0<=y and y<c

def diffusion():
    for i in range(r):
        for j in range(c):
            grid_spread[i][j]=0

    for i in range(r):
        for j in range(c):
            if grid[i][j]!=cleaner:
                spread(i,j)

    for i in range(r):
        for j in range(c):
            grid[i][j]+=grid_spread[i][j]

def unclock_wise(start_row,start_col,end_row,end_col):
    dust=grid[start_row][start_col]

    for col in range(start_col,end_col):
        grid[start_row][col]=grid[start_row][col+1]

    for row in range(start_row,end_row):
        grid[row][end_col]=grid[row+1][end_col]

    for col in range(end_col,start_col,-1):
        grid[end_row][col]=grid[end_row][col-1]

    for row in range(end_row,start_row,-1):
        grid[row][start_col]=grid[row-1][start_col]

    grid[start_row+1][start_col]=dust

def clock_wise(start_row,start_col,end_row,end_col):
    dust=grid[start_row][start_col]

    for row in range(start_row,end_row):
        grid[row][start_col]=grid[row+1][start_col]
    
    for col in range(start_col,end_col):
        grid[end_row][col]=grid[end_row][col+1]

    for row in range(end_row,start_row,-1):
        grid[row][end_col]=grid[row-1][end_col]

    for col in range(end_col,start_col,-1):
        grid[start_row][col]=grid[start_row][col-1]

    grid[start_row][start_col+1]=dust

def cleaning():
    cleanser=[i for i in range(r) if grid[i][0]==cleaner]
    unclock_wise(0,0,cleanser[0],c-1)
    clock_wise(cleanser[1],0,r-1,c-1)

    grid[cleanser[0]][0]=grid[cleanser[1]][0]=-1
    grid[cleanser[0]][1]=grid[cleanser[1]][1]=0

def simulate():
    diffusion()
    cleaning()

for _ in range(t):
    simulate()

answer=sum(grid[i][j] for i in range(r) for j in range(c) if grid[i][j]!=cleaner)
print(answer)

