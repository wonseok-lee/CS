import sys

input=sys.stdin.readline
trial=int(input())

dp=[[0,0,0,0] for _ in range(100000+1)]
dp[1][1]=1
dp[2][2]=1
dp[3][1]=1
dp[3][2]=1
dp[3][3]=1

for i in range(4,100000+1):
    dp[i][1]=(dp[i-1][2]+dp[i-1][3])%1000000009
    dp[i][2]=(dp[i-2][1]+dp[i-2][3])%1000000009
    dp[i][3]=(dp[i-3][2]+dp[i-3][1])%1000000009

while trial:
    n=int(input())
    print(sum(dp[n])%1000000009)
    trial-=1
