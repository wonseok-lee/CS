from collections import defaultdict

def solution(tickets):
    graph=defaultdict(list)
    for a,b in sorted(tickets,reverse=True):
        graph[a].append(b)
    
    route=[]
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)
        
    dfs('ICN')
    
    return route[::-1]
