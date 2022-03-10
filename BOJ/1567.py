import collections
M,N = map(int, input().split())
table=[]
for i in range(N):
    table.append(list(map(int, input().split())))

done=collections.deque()
for i in range(N):
    for j in range(M):
        if table[i][j]==1:
            done.append([i,j])
            
dxdy=[(1,0),(0,1),(-1,0),(0,-1)]
ans=0
while done:
    (x,y)=done.popleft()
    for (dx,dy) in dxdy:
        nxt_x=x+dx
        nxt_y=y+dy
        if (0<=nxt_x<=N-1 and 0<=nxt_y<=M-1) and (table[nxt_x][nxt_y]==0):
            table[nxt_x][nxt_y]=table[x][y]+1
            done.append((nxt_x,nxt_y))

def solve():
    global ans
    for i in range(N):
        for j in range(M):
            if table[i][j]==0:
                print(-1)
                return
            ans = max(ans, table[i][j])
    print(ans-1)
solve()
