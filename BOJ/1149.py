n = int(input().strip())
arr = [[0]*3]
for _ in range(n) :
    row = list(map(int, input().strip().split()))
    arr.append(row)


dp = [[0]*3 for _ in range(n+1)]

for i in range(1, n+1) :
    for j in range(3) :
        if j == 0 :
            dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]

        elif j == 1 :
            dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]

        elif j == 2 :
            dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

print(min(dp[n]))
