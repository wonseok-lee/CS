# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

import sys
from collections import deque

input=sys.stdin.readline
n=int(input())
matrix=[ list(map(str,input().strip())) for _ in range(n)]
dirs=[[1,0],[0,1],[-1,0],[0,-1]]
visited=[[False for _ in range(n)] for _ in range(n)]
# group=0

def bfs(x,y):
    queue=deque()
    queue.append([x,y])
    matrix[x][y]='0'
    group=1
    # print(queue)
    while queue:
        x,y=queue.popleft()
        for dx,dy in dirs:
            nx=x+dx
            ny=y+dy
            if nx<0 or n<=nx or ny<0 or n<=ny:
                continue
            if matrix[nx][ny] =='1':
                matrix[nx][ny] ='0'
                group+=1
                queue.append((nx,ny))
    return group



groups=[]
for i in range(n):
    for j in range(n):
        if matrix[i][j]=='0':
            continue
        # group=0
        # dfs(i,j)
        groups.append(bfs(i,j))


groups.sort()
print(len(groups))
for elt in groups:
    print(elt)



# def dfs(x,y):
#     global group
#     visited[x][y]=True
#     group+=1
#     for dx,dy in dirs:
#         nx=x+dx
#         ny=y+dy
#         if nx<0 or n<=nx or ny<0 or n<=ny:
#             continue
#         if visited[nx][ny]==True:
#             continue
#         if matrix[nx][ny] =='0':
#             continue
#         dfs(nx,ny)

# groups=[]
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j]=='0' or visited[i][j]:
#             continue
#         group=0
#         dfs(i,j)
#         groups.append(group)

# groups.sort()
# print(len(groups))
# for elt in groups:
#     print(elt)
