# 2
# 6
# 22
import sys

input=sys.stdin.readline
trial=int(input())

dp=[[0,0] for _ in range(40+1)]
dp[0]=[1,0]
dp[1]=[0,1]
dp[2]=[1,1]

for i in range(3,41):
    dp[i][0]=dp[i-1][0]+dp[i-2][0]
    dp[i][1]=dp[i-1][1]+dp[i-2][1]

while trial:
    n=int(input())
    x,y=dp[n][0],dp[n][1]
    print(str(x)+' '+str(y))
    trial-=1
