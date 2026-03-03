import sys

input = sys.stdin.readline

a,b=map(int,input().strip().split(' '))
d=dict()
l=[i for i in range(b+1)]
shortcuts = []
for _ in range(a):
    start, end, dist = map(int, input().split())
    if end <= b and (end - start) > dist:
        shortcuts.append((start, end, dist))
    


i=0
while i<b+1 :
    l[i] = min(l[i],l[i-1]+1)
    for start, end, dist in shortcuts:
        if i == start and end <= b:
            if l[end] > l[i] + dist:
                l[end] = l[i] + dist
    i+=1
print(l[b])


