import sys
sys.setrecursionlimit(10000)

input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited=[False for _ in range(n+1)]

def dfs(x):
    visited[x]=True
    for nx in graph[x]:
        if visited[nx]:
            continue
        dfs(nx)

answer=0
for i in range(1,n+1):
    if visited[i]:
        continue
    dfs(i)
    answer+=1

print(answer)