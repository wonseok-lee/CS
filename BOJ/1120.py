a, b = input().strip().split()

min_diff = 50
for i in range(len(b)-len(a)+1) :
    substr = b[i:i+len(a)]
    cnt = 0
    for j in range(len(a)) :
        if a[j] != substr[j] :
            cnt += 1
    min_diff = min(cnt, min_diff)

print(min_diff)
