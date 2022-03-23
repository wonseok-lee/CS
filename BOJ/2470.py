# 5
# -2 4 -99 -1 98

import sys

input=sys.stdin.readline
n=int(input())
nums=sorted(list(map(int,input().split())))

left=0
right=n-1
cand=nums[left]+nums[right]
answer_left=left
answer_right=right

while left<right:
    value=nums[left]+nums[right]
    if abs(value)<abs(cand):
        cand=value
        answer_left=left
        answer_right=right
        if cand==0:
            break
    if value<0:
        left+=1
    else:
        right-=1

print(nums[answer_left],nums[answer_right])

def binary_search(a, left, right, target):
    result = right + 1
    while left <= right:
        mid = left+(right-left) // 2
        if a[mid] >= target:
            result = mid
            right = mid - 1
        else: left = mid + 1
    return result

# best_sum = sys.maxsize
# answer_left, answer_right = 0, 0
# for l in range(n - 1):
#     candidate = binary_search(nums, l + 1, n - 1, -nums[l])
#     if l < candidate - 1 and abs(nums[l] + nums[candidate - 1]) < best_sum:
#         best_sum = abs(nums[l] + nums[candidate - 1])
#         answer_left, answer_right = nums[l], nums[candidate - 1]
    
#     if candidate < n and abs(nums[l] + nums[candidate]) < best_sum:
#         best_sum = abs(nums[l] + nums[candidate])
#         answer_left, answer_right = nums[l], nums[candidate]

# print(answer_left, answer_right)





