# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

import sys
from collections import deque

input=sys.stdin.readline
n=int(input())
v=int(input())
graph=[[] for _ in range(n+1)]
visited=[False for _ in range(n+1)]
for _ in range(v):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

answer=[]
def bfs(k):
    queue=deque()
    queue.append(k)

    while queue:
        v=queue.popleft()
        for node in graph[v]:
            if visited[node]:
                continue
            visited[node]=True
            answer.append(node)
            queue.append(node)

bfs(1)
print(len(answer)-1)