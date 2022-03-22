# 13
# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours

import sys

input=sys.stdin.readline
n=int(input())
answer=set()

for _ in range(n):
    value=str(input().strip())
    answer.add(value)

answer=sorted(answer,key=lambda x: (len(x),x))
for i in range(len(answer)):
    print(answer[i])
