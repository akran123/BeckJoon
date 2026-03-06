from collections import deque
import sys

input = sys.stdin.readline

x, y = map(int, input().split())

grid = []
queue = deque()
unripe_count = 0

for i in range(y):
    row = list(map(int, input().split()))
    for j in range(x):
        if row[j] == 1:
            queue.append((j, i, 0))
        elif row[j] == 0:
            unripe_count += 1
    grid.append(row)

if unripe_count == 0:
    print(0)
    sys.exit()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_days = 0

while queue:
    px, py, days = queue.popleft()
    max_days = days
    
    for i in range(4):
        nx, ny = px + dx[i], py + dy[i]
        
        if 0 <= nx < x and 0 <= ny < y and grid[ny][nx] == 0:
            grid[ny][nx] = 1
            unripe_count -= 1
            queue.append((nx, ny, days + 1))

if unripe_count > 0:
    print(-1)
else:
    print(max_days)
