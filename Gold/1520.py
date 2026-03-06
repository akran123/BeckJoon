import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 재귀 늘리기
y,x =map(int,input().split(' '))

l=[]
for _ in range(y) :
    c=list(map(int,input().split(' ')))
    l.append(c)
dp=[[-1 for _ in range(x)] for _ in range(y)]

visited = set()
stack=[(0,0)]
visited.add((0,0))
end = (x-1,y-1)

dx=[-1,1,0,0]
dy = [0,0,-1,1]
answer=0
'''while stack :
    px,py = stack.pop()
    dp[py][px]+=1
    if (px,py)==end :
        answer+=1

    for i in range(4) :
        nx=px+dx[i]
        ny =py+dy[i]
        if 0<=nx<x and 0<=ny<y and l[ny][nx]<l[py][px] and (nx,ny) not in visited :
            stack.append((nx,ny))


    print(stack)'''

def asdf(px,py) :
    global end
    if (px,py)==end :
        return 1
    
    if dp[py][px]!=-1 :
        return dp[py][px]
    dp[py][px]=0
    for i in range(4) :
        nx=px+dx[i]
        ny =py+dy[i]
        if 0<=nx<x and 0<=ny<y and l[ny][nx]<l[py][px] :
            dp[py][px]+=asdf(nx,ny)
    return dp[py][px]

print(asdf(0,0))