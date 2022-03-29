# 6
# 5
# 1 2
# 1 3
# 3 4
# 2 3
# 4 5

import sys
from collections import deque

input=sys.stdin.readline

n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]
visited=[-1 for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(k):
    queue=deque()
    queue.append(k)
    while queue:
        x=queue.popleft()
        for node in graph[x]:
            if visited[node]!=-1:
                continue
            visited[node]=visited[x]+1
            queue.append(node)

visited[0]=0
visited[1]=0

bfs(1)

answer=0
for i in visited[2:]:
    if i<=2 and i!=-1:
        answer+=1
print(answer)
