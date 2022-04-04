# 11
# 8 3 2 4 8 7 2 4 0 8 8

import sys

input=sys.stdin.readline

n=int(input())
nums=list(map(int, input().split()))
dp=[[0 for _ in range(21)] for _ in range(n)]

dp[0][nums[0]] = 1
# dp[i][j]: 길이가 i까지의 결과가 j인 경우의 수
# dp[i][후보값]+=dp[i-1][j]
# 후보값=j-nums[i]
for i in range(1,n-1):
    for j in range(21):
        candi=[j-nums[i],j+nums[i]]
        for elt in candi:
            if elt<0 or 20<elt:
                continue
            else:
                dp[i][elt]+=dp[i-1][j]

print(dp[n-2][nums[n-1]])

