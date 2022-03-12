def solution(clothes):
    answer = 1
    counters={}
    for name,category in clothes:
        count=counters.get(category,0)
        counters[category]=count+1
        
    for i in counters.values():
        answer *= (i+1)
    return answer - 1
