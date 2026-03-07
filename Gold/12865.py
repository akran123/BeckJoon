import heapq
from itertools import combinations
n,k = map(int,input().split(' '))

l=[]
d=dict()
dp=[0]*(k+1)
for _ in range(n) :
    w,v =map(int,input().split(' '))
    for j in range(n,w-1,-1) :
        if dp[j]<dp[j-w]+v :
            dp[j]=dp[j-w]+v
        else :
            dp[j]=v
print(dp[k])