import sys

input=sys.stdin.readline

N,M,x,y,K=map(int,input().split())
matrix=[]
for _ in range(N):
    temp=list(map(int,input().split()))
    matrix.append(temp)

orders=list(map(int,input().split()))
dice=[0 for _ in range(7)]

dirs=[[0,0],[0,1],[0,-1],[-1,0],[1,0]]
answer=0
up,front,right=1,2,3
# dice[1],dice[2],dice[3]=up,front,right

def move(order):
    global x,y,up,front,right
    dx,dy=dirs[order]
    nx,ny=x+dx,y+dy

    if nx<0 or N<=nx or ny<0 or M<=ny:
        # print('h')
        return
    

    if order==1:
        up,front,right=7-right,front,up
    elif order==2:
        up,front,right=right,front,7-up
    elif order==3:
        up,front,right=front,7-up,right
    else:
        up,front,right=7-front,up,right
        
    bottom=7-up

    if matrix[nx][ny]==0:
        matrix[nx][ny]=dice[bottom]
    else:
        dice[bottom]=matrix[nx][ny]
        matrix[nx][ny]=0

    print(dice[up])
    x,y=nx,ny

for order in orders:
    move(order)
