def solution(answers):
    ans1=[1,2,3,4,5]
    ans2=[2,1,2,3,2,4,2,5]
    ans3=[3,3,1,1,2,2,4,4,5,5]
    s1,s2,s3 = 0,0,0
    result=[]
    for idx, num in enumerate(answers):
        
        if num == ans1[idx%len(ans1)]:
            s1+=1
        if num == ans2[idx%len(ans2)]:
            s2+=1
        if num == ans3[idx%len(ans3)]:
            s3+=1
    
    for idx, score in enumerate([s1,s2,s3]):
        if score==max([s1,s2,s3]):
            result.append(idx+1)
    return result
