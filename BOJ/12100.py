import sys
input=sys.stdin.readline

NONE=-1
move_nums=5
answer=0

n=int(input())
matrix=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    matrix.append(temp)

matrix_copy=[[0 for _ in range(n)] for _ in range(n)]

temp=[[0 for _ in range(n)] for _ in range(n)]

move_dirs = [0 for _ in range(move_nums)]

def get_max_block_num():
    return max([matrix[i][j] for i in range(n) for j in range(n)])

def rotate():
    for i in range(n):
        for j in range(n):
            matrix_copy[i][j]=0

    for i in range(n):
        for j in range(n):
            matrix_copy[i][j]=matrix[n-j-1][i]
    
    for i in range(n):
        for j in range(n):
            matrix[i][j]=matrix_copy[i][j]
    

def drop():
    for i in range(n):
        for j in range(n):
            matrix_copy[i][j]=0
    
    for j in range(n):
        keep,nxt_row=NONE,n-1

        for i in range(n-1,-1,-1):

            if not matrix[i][j]:
                continue
            
            if keep==NONE:
                keep=matrix[i][j]
            
            elif keep==matrix[i][j]:
                matrix_copy[nxt_row][j]=keep*2
                keep=NONE
                nxt_row-=1
            
            else:
                matrix_copy[nxt_row][j]=keep
                keep=matrix[i][j]
                nxt_row-=1
        
        if keep!=NONE:
            matrix_copy[nxt_row][j]=keep
            nxt_row-=1

    for i in range(n):
        for j in range(n):
            matrix[i][j]=matrix_copy[i][j]

def tilt(move_dir):
    for _ in range(move_dir):
        rotate()

    drop()

    for _ in range(4-move_dir):
        rotate()


def simulate():
    global answer

    for i in range(n):
        for j in range(n):
            temp[i][j]=matrix[i][j]
    
    for move_dir in move_dirs:
        tilt(move_dir)
    
    answer=max(answer,get_max_block_num())

    for i in range(n):
        for j in range(n):
            matrix[i][j]=temp[i][j]

def search_max_num(cnt):
    if cnt==move_nums:
        simulate()
        return
    for i in range(4):
        move_dirs[cnt]=i
        search_max_num(cnt+1)

search_max_num(0)
print(answer)


