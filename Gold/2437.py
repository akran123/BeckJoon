from itertools import combinations

a=int(input())
l=list(map(int,input().split(' ')))
l.sort()

target=1
for i in l :
    if target<i :
        break
    target+=i
print(target)

