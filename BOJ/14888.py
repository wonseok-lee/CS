# 2
# 5 6
# 0 0 1 0

import sys

n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))
operators=list(map(int,sys.stdin.readline().split()))

max_val=-sys.maxsize
min_val=sys.maxsize

def operator(x,oper,y):
    if oper==0:
        return x+y
    elif oper==1:
        return x-y
    elif oper==2:
        return x*y
    elif oper==3:
        if x<0:
            return -((-x//y))
        else:
            return x//y

def dfs(k,value):
    if k==n-1:
        global max_val, min_val
        max_val=max(max_val,value)
        min_val=min(min_val,value)
    else:
        for cand in range(4):
            if operators[cand]>=1:
                operators[cand]-=1
                dfs(k+1,operator(value,cand,nums[k+1]))
                operators[cand]+=1

dfs(0,nums[0])

print(max_val)
print(min_val)

