import sys

n, m = map(int, input().split())
arr = list()
for i in range(n):
    arr.append(input())

def gen_cut_arr(y, x) :
    cut_arr = []
    for i in range(y, y+8) :
        row = []
        for j in range(x, x+8) :
            row.append(arr[i][j])

        cut_arr += row
    return cut_arr


base1 = ['W', 'B'] * 4
base2 = ['B', 'W'] * 4

WB = []
for i in range(8) :
    if i % 2 == 0 :
        WB += base1
    else :
        WB += base2

BW = []
for i in range(8) :
    if i % 2 == 0 :
        BW += base2
    else :
        BW += base1

ANS = sys.maxsize
for y in range(n-7) :
    for x in range(m-7) :
        cut_arr_1d = gen_cut_arr(y, x)

        cnt_w = 0
        cnt_b = 0
        for i in range(64) :
            if cut_arr_1d[i] != WB[i] :
                cnt_w += 1
                continue
            if cut_arr_1d[i] != BW[i] :
                cnt_b += 1
                continue

        ANS = min(ANS, cnt_w, cnt_b)

print(ANS)
