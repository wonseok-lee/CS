import sys

input=sys.stdin.readline
n,s,m=map(int,input().split())
nums=list(map(int,input().split()))

dp=[[-1 for _ in range(m+1)] for _ in range(n+1)]
dp[0][s]=s

for i in range(1,n+1):
    answer=-1
    for j in range(m+1):
        if dp[i-1][j]==-1:
            continue
        candi=[j-nums[i-1],j+nums[i-1]]
        for elt in candi:
            if elt<0 or elt>m:
                continue
            dp[i][elt]=dp[i-1][j]
            answer=max(answer,elt)
# print(max(dp[]))
print(answer)
