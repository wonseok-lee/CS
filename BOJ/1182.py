import sys

n,s=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
answer=0

def dfs(val,i):
    if i==n:
        global answer
        if val==s:
            answer+=1
    else:
        dfs(val+nums[i],i+1)
        dfs(val,i+1)

dfs(0,0)
if s==0:
    answer-=1
print(answer)



