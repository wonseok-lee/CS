# 2
# 5
# 50 10 100 20 40
# 30 50 70 10 60
# 7
# 10 30 10 50 100 20 40
# 20 40 30 50 60 20 80

import sys

input=sys.stdin.readline

trial=int(input())
while trial:
    n=int(input())

    dp=[[0,0] for _ in range(n)]
    matrix=[]
    for _ in range(2):
        temp=list(map(int,input().split()))
        matrix.append(temp)

    if n==1:
        print(max(matrix[0][0],matrix[1][0]))
    else:
        dp[0][0]=matrix[0][0]
        dp[0][1]=matrix[1][0]
        
        dp[1][1]=dp[0][0]+matrix[1][1]
        dp[1][0]=dp[0][1]+matrix[0][1]

        for i in range(2,n):
            dp[i][0]=max(dp[i-1][1],dp[i-2][1])+matrix[0][i]
            dp[i][1]=max(dp[i-1][0],dp[i-2][0])+matrix[1][i]

        # print(dp)
        print(max(dp[n-1]))
    trial-=1

