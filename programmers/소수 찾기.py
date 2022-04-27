import math
from itertools import permutations


def solution(numbers):
    def check_prime(num):
        if num==0 or num==1:
            return False
        for i in range(2,int(math.sqrt(num))+1):
            if num % i==0:
                return False
        return True
                            
    nums = [n for n in numbers]
    per = []
    for i in range(1, len(numbers)+1):
        per += list(permutations(nums, i))
    new_nums = set(int(("").join(p)) for p in per)
    answer = 0

    for num in new_nums:
        if check_prime(num):
            answer+=1
            
    return answer
