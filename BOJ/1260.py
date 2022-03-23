# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

import sys
from collections import deque, defaultdict
input=sys.stdin.readline
output=sys.stdout.write

n,m,start=map(int,input().split())
matrix=defaultdict(list)
for _ in range(m):
    x,y=map(int,input().split())
    matrix[x].append(y)
    matrix[y].append(x)

for i in range(1,n+1):
    matrix[i]=sorted(matrix[i])

visited=[False for _ in range(n+1)]

def dfs(v):
    visited[v]=True
    # print(v)
    output(str(v)+' ')
    for i in matrix[v]:
        if visited[i]==True:
            continue
        dfs(i)

def bfs(v):
    visited=[False for _ in range(n+1)]
    queue=deque([v])
    visited[v]=True
    while queue:
        node=queue.popleft()
        # print(node)
        output(str(node)+' ')
        for nxt_node in matrix[node]:
            if visited[nxt_node]==True:
                continue
            visited[nxt_node]=True
            queue.append(nxt_node)

dfs(start)
print()
bfs(start)