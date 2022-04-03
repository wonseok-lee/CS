# import sys

# input=sys.stdin.readline
# n=int(input())
# nums=[0]+list(map(int,input().split()))

# dp=[0 for _ in range(n+1)]

# for i in range(1,n+1):
#     for x in range(1,i+1):
#         dp[i]=max(dp[i],dp[i-x]+nums[x])

# print(dp[x])


import sys

input=sys.stdin.readline
n=int(input())
nums=[0]+list(map(int,input().split()))



