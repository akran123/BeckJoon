import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split(' '))

l=[[] for _ in range(n)]
for _ in range(m) :
    a,b = map(int,input().split(' '))
    l[a].append(b)
    l[b].append(a)
'''for i in range(n) :
    
    stack=deque()
    stack.append(i)
    visited=set()
    visited.add(i)
    while stack :
        t = stack.pop()
        visited.add(t)
        tmp=l[t]
        mode=0
        e=[]
        for k in range(n) :
            if tmp[k]==1 and k not in visited and t!=k:
                stack.append(k)
                e.append(k)
        if len(e)==0 :
            if len(visited)<5 :
                visited.remove(t)
        
    if len(visited)>=5 :
        answer=1
        break
print(answer)'''
answer=0
visited=[False]*n
def asdf(i,depth) :
    global answer
    
    if answer ==1 :
        return
    if depth ==4 :
        answer =1
        return
    tmp=l[i]
    for k in tmp :
        if visited[k]==False:
            visited[k]=True
            asdf(k,depth+1)
            visited[k]=False

for i in range(n) :
    visited[i]=True
    asdf(i,0)
    visited[i]=False
    if answer ==1 :
        break
print(answer)