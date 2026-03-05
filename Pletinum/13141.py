from collections import deque
import heapq
a,b= map(int,input().split(' '))

l=[[10**9] *(a+1) for i in range(a+1)]
s=set()
for i in range(1,a+1) :
    l[i][i]=0
for i in range(b) :
    c=list(map(int,input().split(' ')))
    if c[2]<l[c[0]][c[1]] :
        l[c[0]][c[1]]=c[2]
        l[c[1]][c[0]]=c[2]
    

    s.add((c[0],c[1],c[2]))

for k in range(1,a+1) :
    for i in range(1,a+1) :
        for j in range(1,a+1) :
            if l[i][j]> l[i][k]+l[k][j] :
                l[i][j] = l[i][k]+l[k][j]
min_time=10**9
for i in range(1,a+1) :
    max_time=0

    for u,y,p in s :
        burn_time = (l[i][u]+l[i][y]+p)/2

        if burn_time>max_time :
            max_time = burn_time
    if max_time<min_time :
        min_time = max_time
print(min_time)

