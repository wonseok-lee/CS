# 9 5 3
# 1 3
# 4 3
# 5 4
# 5 6
# 6 7
# 2 3
# 9 6
# 6 8
# 5
# 4
# 8

import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

n,r,q=map(int,input().split())
dp=[0 for _ in range(n+1)]
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(root,prev):
    global dp
    dp[root]=1
    for node in graph[root]:
        if node==prev:
            continue
        dfs(node,root)
        dp[root]+=dp[node]

dfs(r,-1)
# print(dp)
for _ in range(q):
    print(dp[int(input())])
