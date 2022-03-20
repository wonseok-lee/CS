# 4 2


import sys

n,m = map(int,sys.stdin.readline().split())

selected=[0 for _ in range(m)]
used=[0 for _ in range(n+1)]

def dfs(k):
    if k==m:
        for x in selected:
            sys.stdout.write(str(x)+' ')
        sys.stdout.write('\n')
        return
    else:
        for cand in range(1,n+1):
            selected[k]=cand
            dfs(k+1)
            selected[k]=0


dfs(0)


