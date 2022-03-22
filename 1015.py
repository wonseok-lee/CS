# 8
# 4 1 6 1 3 6 1 4

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
B = [(i, x) for i, x in enumerate(a)]

B=sorted(B, key=lambda x: (x[1],x[0]))
p=[0 for _ in range(n)]

for idx,elt in enumerate(B):
    i,val=elt
    p[i]=idx
for i in p:
    sys.stdout.write(str(i)+' ')
