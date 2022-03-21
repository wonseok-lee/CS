import sys

input=sys.stdin.readline

n=int(input())
grades=[]
for _ in range(n):
    val=input().split()
    grades.append(val)
grades=sorted(grades,key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),str(x[0])))

for grade in grades:
    sys.stdout.write(str(grade[0]))
    sys.stdout.write('\n')



