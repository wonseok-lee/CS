# 3
# 0 1 0
# 0 0 1
# 1 0 0

import sys
from collections import deque

input=sys.stdin.readline
n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]

# print(matrix)
def bfs(v):
    visited = [0 for _ in range(n)]
    queue=deque()
    queue.append(v)

    while queue:
        x=queue.popleft()
        for node in range(n):
            if visited[node]==1:
                continue
            if matrix[x][node]==0:
                continue
            visited[node]=1
            queue.append(node)
    for i in range(n):
        print(visited[i], end=' ')
    print()


for i in range(n):
    bfs(i)
