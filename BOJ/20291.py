# 8
# sbrus.txt
# spc.spc
# acm.icpc
# korea.icpc
# sample.txt
# hello.world
# sogang.spc
# example.txt

import sys

input=sys.stdin.readline

n=int(input())
counters={}
for _ in range(n):
    pre, format=map(str,input().strip().split('.'))
    count=counters.get(format,0)
    counters[format]=count+1
counters=sorted(counters.items(),key=lambda x: x[0])

for i in range(len(counters)):
    format, num=counters[i]
    print(format,num)






