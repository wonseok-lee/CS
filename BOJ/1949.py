import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

n=int(input())

nums=[0]+list(map(int,input().split()))
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dp=[[0,0] for _ in range(n+1)]

def dfs(root,prev):
    dp[root][1]+=nums[root]
    for node in graph[root]:
        if node==prev:
            continue
        print(dp)
        dfs(node,root)
        print('-'*30)
        dp[root][0]+=max(dp[node])
        dp[root][1]+=dp[node][0]

dfs(1,-1)
print(dp)
print(max(dp[1]))

