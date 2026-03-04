import sys
from collections import deque

input = sys.stdin.readline
a=int(input())
for _ in range(a) :
    x,y,count= map(int,input().strip().split(' '))
    l=[[0 for _ in range(x)] for _ in range(y)]
    visted = set()
    for _ in range(count) :
        c,d= map(int,input().strip().split(' '))

        l[d][c]=1

    dx=[-1,1,0,0]
    dy = [0,0,-1,1]



    result=0

    for i in range(x) :
        for k in range(y) :
            if l[k][i] ==1 and (i,k) not in visted :
                
                queue = deque([(i,k)])
                result+=1
                while queue :
                    
                    tmp_x,tmp_y = queue.popleft()
                    for p in range(4) :
                        nx,ny = tmp_x+dx[p],tmp_y+dy[p]

                        if 0<=nx<x and 0<=ny<y :
                            if l[ny][nx]==1 and (nx,ny) not in visted :
                                visted.add((nx,ny))
                                queue.append((nx,ny))

            
                

    print(result)
