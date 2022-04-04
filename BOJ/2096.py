# 3
# 1 2 3
# 4 5 6
# 4 9 0

import sys

input=sys.stdin.readline

n=int(input())

mini=[[0,0,0] for _ in range(2)]
maxi=[[0,0,0] for _ in range(2)]

for _ in range(n):
    matrix_row = list(map(int,input().split()))
    mini[1][0]=matrix_row[0]+min(mini[0][1],mini[0][0])
    mini[1][1]=matrix_row[1]+min(mini[0][0],mini[0][1],mini[0][2])
    mini[1][2]=matrix_row[2]+min(mini[0][2],mini[0][1])

    maxi[1][0]=matrix_row[0]+max(maxi[0][1],maxi[0][0])
    maxi[1][1]=matrix_row[1]+max(maxi[0][0],maxi[0][1],maxi[0][2])
    maxi[1][2]=matrix_row[2]+max(maxi[0][2],maxi[0][1])

    mini[0][0],mini[0][1],mini[0][2]=mini[1][0],mini[1][1],mini[1][2]
    maxi[0][0],maxi[0][1],maxi[0][2]=maxi[1][0],maxi[1][1],maxi[1][2]


print(max(maxi[1]), end=' ')
print(min(mini[1]))
