import sys

input=sys.stdin.readline

trial=int(input())

dp=[[0 for _ in range(10)] for _ in range(64+1)]

for i in range(10):
    dp[1][i]=1

for i in range(2,64+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j]+=dp[i-1][k]

while trial:
    n=int(input())
    print(sum(dp[n]))
    trial-=1
