# 5 17

import sys
from collections import deque

input=sys.stdin.readline
n,k=map(int,input().split())
visited=[-1 for _ in range(10001)]

def bfs(x):
    queue=deque()
    queue.append(x)
    visited[x]=0

    def move(x,dist):
        if x<0 or x>10000 or visited[x]!=-1:
            return
        visited[x]=dist
        queue.append(x)

    while queue:
        x=queue.popleft()
        move(x-1,visited[x]+1)
        move(x+1,visited[x]+1)
        move(x*2,visited[x]+1)
bfs(n)
print(visited[k])

# from collections import deque

# def bfs():
#     q = deque()
#     q.append(n)
#     while q:
#         x = q.popleft()
#         if x == k:
#             print(dist[x])
#             return
#         for nx in (x-1, x+1, x*2):
#             if 0 <= nx <= MAX and not dist[nx]:
#                 dist[nx] = dist[x]+1
#                 q.append(nx)

# MAX = 100000
# n, k = map(int, input().split())
# dist = [0]*(MAX+1)
# bfs()