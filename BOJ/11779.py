from re import L
import sys
si=sys.stdin.readline
n=int(si())

grid=[list(map(int,si().split())) for _ in range(n)]

wall=[[False for _ in range(n)]for _ in range(n)]
total=0
def initialize_wall():
    for i in range(n):
        for j in range(n):
            wall[i][j]=False

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def go(x,y,d1,d2):
    return in_range(x-d1,y+d1) and in_range(x-d1-d2,y+d1-d2) and in_range(x-d2,y-d2)

def draw(x,y,d1,d2):
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    # dirs=[[1,-1],[-1,1],[1,1],[-1,-1]]
    move_nums=[d1,d2,d1,d2]

    initialize_wall()

    for dx,dy,move_num in zip(dxs,dys,move_nums):
        for _ in range(move_num):
            x,y=x+dx,y+dy
            wall[x][y]=True

def get_score(x,y,d1,d2):
    size=[0 for _ in range(5)]

    draw(x,y,d1,d2)
    for i in range(x-d2):
        for j in range(y+d1-d2+1):
            if wall[i][j]:
                break

            size[0]+=grid[i][j]
    
    for i in range(x-d2,n):
        for j in range(y):
            if wall[i][j]:
                break

            size[1]+=grid[i][j]

    for i in range(x-d1+1):
        for j in range(n-1,y+d1-d2,-1):
            if wall[i][j]:
                break

            size[2]+=grid[i][j]

    for i in range(x-d1+1,n):
        for j in range(n-1,y-1,-1):
            if wall[i][j]:
                break

            size[3]+=grid[i][j]

    size[4]=total-sum(size[:4])
    return max(size)-min(size)

total=sum([grid[i][j] for i in range(n) for j in range(n)])

answer=sys.maxsize

for i in range(n):
    for j in range(n):
        for d1 in range(1,n):
            for d2 in range(1,n):
                if go(i,j,d1,d2):
                    answer=min(answer,get_score(i,j,d1,d2))
print(answer)

