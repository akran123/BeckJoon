from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split(' ')) #사람, 파티
queue = deque()
a=list(map(int,input().split(' ')))
know=set()
for i in range(a[0]) :
    queue.append(a[i+1])
    know.add(a[i+1])

d=dict()
for i in range(n) :
    d[i+1]=[]

graph=[[] for i in range(m+1)]
for i in range(m) :
    c=list(map(int,input().split(' ')))
    for k in range(1,len(c)) :
        d[c[k]].append(i+1)
        graph[i+1].append(c[k])



while queue :
    known = queue.popleft()
    parties = d[known]
    if parties is not None :
        for i in parties :
            tmp =graph[i]
            for k in tmp :
                if k not in know :
                    know.add(k)
                    queue.append(k)
know = list(know)
answer=set()
for i in know :
    t=d[i]
    for k in t :
        answer.add(k)
print(m-len(answer))
