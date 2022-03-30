import sys
input=sys.stdin.readline

n=int(input())
nums=list(map(int,input().split()))

nums=sorted(nums)

print(nums)
answer=0

if n//2==0:
    for i in range(n//2):
        answer+=
