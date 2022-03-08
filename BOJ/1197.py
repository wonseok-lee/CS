import sys

v, e = map(int, sys.stdin.readline().split())
arr = []
for _ in range(e):
    a, b, w = map(int, sys.stdin.readline().split())
    arr.append((w,a,b))

arr.sort(key=lambda x: x[0])
parent = list(range(v + 1))

def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

sum = 0
for w, a, b in arr:
    if find(a) != find(b):
        union(a, b)
        sum += w

print(sum)
