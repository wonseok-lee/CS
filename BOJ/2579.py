import sys

input=sys.stdin.readline

n=int(input())
a=[0]
if n==0:
    print(0)
    sys.exit(0)
else:
    for _ in range(1,n+1):
        a.append(int(input()))
if n==1:
    print(a[1])
    sys.exit(0)

dp=[[0,0] for _ in range(n+1)]

dp[1][0]=a[1]
dp[2][0]=a[2]
dp[2][1]=a[1]+a[2]

for i in range(3,n+1):
    dp[i][0]=max(dp[i-2][0]+a[i],dp[i-2][1]+a[i])
    dp[i][1]=dp[i-1][0]+a[i]

print(max(dp[n][0],dp[n][1]))
