# 2
# 5 3
# 8 1 7 3 1
# 3 6 1
# 3 4
# 2 13 7
# 103 11 290 215


import sys

input=sys.stdin.readline

def binary_search(tmp,target):
    left,right=0,len(tmp)-1
    result=-1
    while left<=right:
        mid=left+(right-left)//2
        if tmp[mid]<target:
            result=mid
            left=mid+1
        else:
            right=mid-1
    return result



Trial=int(input())
for _ in range(Trial):
    answer=0
    na,nb=map(int,input().split())
    a=list(map(int,input().split()))
    b=sorted(list(map(int,input().split())))
    for x in a:
        temp=binary_search(b,x)+1
        answer+=temp
    print(answer)
