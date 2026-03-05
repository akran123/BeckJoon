import sys
import heapq
input = sys.stdin.readline

n,m,target =map(int,input().strip().split(' ')) # 학생, 도로, x 마을

graph = [[] for _ in range(n+1)]
for _ in range(m) :
    start,end,price = map(int,input().strip().split(' '))
    graph[start].append((end,price))


def asdf(n,i,target) :
    global graph
    distance = [10**9]*(n+1)
    q=[]
    heapq.heappush(q,(0,i))
    distance[i]=0
    while q :
        dist,now = heapq.heappop(q)
        
        if distance[now]<dist :
            continue

        for x,y in graph[now] :
            if distance[x]>dist+y :
                heapq.heappush(q,(dist+y,x))
                distance[x]=dist+y

    return distance[target]

max=0
for i in range(1,n+1) :
    go = asdf(n,i,target)
    back = asdf(n,target,i)
    if go+back>max :
        max = go+back
print(max)