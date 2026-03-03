import sys

input = sys.stdin.readline

a=int(input())

l=[0]*(a+1)

for i in range(2,a+1) :
    tmp =[]
    if i%2 ==0 :
        tmp.append(l[i//2]+1)
    if i%3==0 :
        tmp.append(l[i//3]+1)
    tmp.append(l[i-1]+1)
    m=min(tmp)
    l[i]=m
print(l[a])