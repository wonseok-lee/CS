import sys
input=sys.stdin.readline


word=['0']+list(map(str,input().strip()))
n=len(word)
dp=[0 for _ in range(n)]
dp[0]=1
dp[1]=1

for i in range(2,n):
    if int(word[i])>0:
        dp[i]+=dp[i-1]% 1000000
    temp=10*int(word[i-1])+int(word[i])
    if 10<=temp and temp<=26:
        dp[i]+=dp[i-2]% 1000000
if word[1]=='0':
    print(0)
else:
    print(dp[-1]% 1000000)