# 4 6
# a t c i s w

import sys

l,c=map(int,sys.stdin.readline().split())
strings=sorted(list(map(str,sys.stdin.readline().split())))

moeum=['a', 'e', 'i', 'o', 'u']
# moeum_num=0
# jaeum_num=0

selected=[0 for _ in range(l)]
used=[0 for _ in range(c)]


answer=0

def dfs(k):
    if k==l:
        moeum_num,jaeum_num=0,0
        for x in selected:
            temp=strings[x]
            if temp in moeum:
                moeum_num+=1
            else:
                jaeum_num+=1

        if (moeum_num>=1) and (jaeum_num>=2):
            answer=''
            for x in selected:
                answer+=strings[x]
            sys.stdout.write(answer)
            sys.stdout.write('\n')
    else:
        start=-1 if k==0 else selected[k-1]
        for i in range(start+1,c):
            selected[k]=i
            dfs(k+1)
            selected[k]=0

dfs(0)

# import sys
# input = sys.stdin.readline
# m, n = map(int, input().split(' '))
# chars = sorted(input().strip().split(' '))
# used = [0] * n
# selected = [0] * m

# def is_vowel(x: str):
#     return x in "aeiou"

# def rec_func(k):
#     if k == m:
#         vowel, consonant = 0, 0
#         for x in selected:
#             if is_vowel(chars[x]):
#                 vowel += 1
#             else:
#                 consonant += 1

#         if (vowel >= 1) and (consonant >= 2):
#             for x in selected:
#                 print(chars[x], end='')
#             print()

#     else:
#         st = -1 if k == 0 else selected[k - 1]
#         for i in range(st + 1, n):
#             selected[k] = i
#             rec_func(k + 1)
#             selected[k] = 0

# rec_func(0)
