import sys

n=int(sys.stdin.readline())
col=[0 for _ in range(n)]
answer=0

def queen(r0,c0,r1,c1):
    if c0==c1:
        return True
    if abs(r0-r1)==abs(c0-c1):
        return True
    return False

def dfs(row):
    if row==n:
        global answer
        answer+=1
    else:
        for cand in range(n):
            possible=True
            for i in range(row):
                if queen(row,cand,i,col[i]):
                    possible=False
                    break
            if possible:
                col[row]=cand
                dfs(row+1)
                col[row]=0

dfs(0)
print(answer)



