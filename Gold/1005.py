import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
answer=[]
for _ in range(T) :
    N,K =map(int,input().strip().split(' ')) # 건물 개수,규칙 개수
    time = [0 for i in range(N+1)]

    c=list(map(int,input().strip().split(' ')))
    for i in range(1,len(c)+1) :
        time[i] = c[i-1]

    l=[[] for _ in range(N+1)]
    p=[0 for _ in range(N+1)]
    for _ in range(K) :
        start,end = map(int,input().split(' '))
        l[start].append(end)
        p[end]+=1
    target = int(input())
    queue=deque()
    dp=[0 for _ in range(N+1)]
    for i in range(1,len(p)) :
        if p[i]==0 :
            queue.append(i)
            dp[i]=time[i]
    
    
    while queue :
        e=queue.popleft()
        tmp=l[e]
        for i in tmp :
            dp[i] = max(dp[i],dp[e]+time[i])
            p[i]-=1
            if p[i]==0 :
                queue.append(i)
    answer.append(dp[target])

for i in answer :
    print(i)




