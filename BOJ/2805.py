# 4 7
# 20 15 10 17

import sys

input=sys.stdin.readline

n,h=map(int,input().split())
trees=sorted(list(map(int,input().split())))

left,right=0,sys.maxsize
answer=0

while left<=right:
    mid=left+(right-left)//2

    temp=0
    for tree in trees:
        if tree>=mid:
            temp+=tree-mid
    if temp<=h:
        answer=mid
        right=mid-1
    else:
        left=mid+1

print(answer)










