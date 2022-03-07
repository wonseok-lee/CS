a = int(input())

dp = []
dp.append((1, 0))
dp.append((0, 1))
dp.append((1, 1))

for i in range(3, 41) :
    p2 = dp[i-2]
    p1 = dp[i-1]

    y, x = p2[0] + p1[0], p2[1] + p1[1]
    dp.append((y, x))

for _ in range(a) :
    n = int(input())
    print(' '.join(map(str, dp[n])))
