# 4 2
# 9 7 9 1

import sys

input=sys.stdin.readline

n,m=map(int,input().split())
nums=sorted(list(map(int,input().split())))

used=[0 for _ in range(n+1)]
selected=[0 for _ in range(m)]

def dfs(k):
    if k==m:
        for x in selected:
            sys.stdout.write(str(x)+' ')
        sys.stdout.write('\n')
    else:
        last_cand=0
        for cand in range(n):
            if used[cand]==1 or nums[cand]==last_cand:
                continue
            last_cand=nums[cand]
            selected[k]=nums[cand]
            used[cand]=1
            dfs(k+1)
            selected[k]=0
            used[cand]=0

dfs(0)
