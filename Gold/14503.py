import sys

input = sys.stdin.readline

y, x = map(int, input().split(' '))
sy, sx, d = map(int, input().split(' '))
l = []
for _ in range(y):
    c = list(map(int, input().split(' ')))
    l.append(c)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

count = 0
px, py, di = sx, sy, d

while True:
    if l[py][px] == 0:
        count += 1
        l[py][px] = 2
    
    tmp = []
    for i in range(4):
        nx, ny = px + dx[i], py + dy[i]
        if 0 <= nx < x and 0 <= ny < y and l[ny][nx] == 0:
            tmp.append((nx, ny))
    
    if len(tmp) == 0:
        bx, by = px - dx[di], py - dy[di]
        if 0 <= bx < x and 0 <= by < y and l[by][bx] != 1:
            px, py = bx, by
        else:
            break
    else:
        di = (di + 3) % 4
        nx, ny = px + dx[di], py + dy[di]
        if 0 <= nx < x and 0 <= ny < y and l[ny][nx] == 0:
            px, py = nx, ny

print(count)