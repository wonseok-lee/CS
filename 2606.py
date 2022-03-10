from sys import stdin
from collections import defaultdict

dic=defaultdict(list)
k = int(stdin.readline().strip())
n = int(stdin.readline().strip())

for j in range(n):
    a, b = map(int,stdin.readline().strip().split())
    dic[a].append(b)
    dic[b].append(a)

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)
visited = []
dfs(1, dic)
print(len(visited)-1)
