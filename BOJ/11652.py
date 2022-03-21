import sys

input=sys.stdin.readline
n=int(input())

counters={}
for _ in range(n):
    val=int(input())
    count=counters.get(val,0)
    counters[val]=count+1

counters=sorted(counters.items(), key=lambda x: (-x[1],x[0]))

print(counters)



