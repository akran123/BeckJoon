import sys
a=int(input())
l=[int(input()) for _ in range(a)]

stairs =[0 for i in range(a+1)]


if a==1 :
    print(l[0])
elif a==2 :
    print(l[0]+l[1])
else :
    
    stairs[1]=l[0]
    stairs[2]=l[1]+l[0]
    stairs[3]=max(l[0]+l[2],l[1]+l[2])
    for i in range(4,a+1) :
        stairs[i]=max(stairs[i-2]+l[i-1],stairs[i-3]+l[i-1]+l[i-2])
    print(stairs[a])
