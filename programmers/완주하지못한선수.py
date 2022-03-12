import collections


def solution(participant, completion):
    answer=''
    counters={}
    for name in completion:
        count=counters.get(name,0)
        counters[name]=count+1

    for name in participant:
        count=counters.get(name,0)
        counters[name]=count-1
        if (count:=counters.get(name)) ==-1:
            answer=name
    return answer
