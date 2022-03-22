# 7
# 6 1
# 7 2
# 9 1
# 10 2
# 0 1
# 3 1
# 4 1

import sys

input=sys.stdin.readline
n=int(input())
points=[[] for _ in range(n+1)]
for _ in range(n):
    location,color = map(int,input().split())
    points[color].append(location)

points.sort()
answer=0

def help(tmp):
    val=0
    for idx,elt in enumerate(tmp):
        if idx==0:
            val+=tmp[idx+1]-elt
        elif idx==len(tmp)-1:
            val+=elt-tmp[idx-1]
        else:
            val+=min(abs(tmp[idx+1]-elt),abs(elt-tmp[idx-1]))
    return val

for i in range(1,n+1):
    temp=sorted(points[i])
    answer+=help(temp)
    # print(answer)
print(answer)
            

# import sys
# n = int(sys.stdin.readline())

# a = [[] for _ in range(n + 1)]

# for i in range(n):
#     coord, color = map(int, sys.stdin.readline().split())
#     a[color].append(coord)

# def toLeft(color, i):
#     if i == 0:
#         return 1000000
#     return a[color][i] - a[color][i - 1]

# def toRight(color, i):
#     if i + 1 == len(a[color]):
#         return 1000000
#     return a[color][i + 1] - a[color][i]


# ans = 0
# for color in range(1, n + 1):
#     a[color].sort()
#     for i in range(len(a[color])):
#         ans += min(toLeft(color, i), toRight(color, i))

# print(ans)


