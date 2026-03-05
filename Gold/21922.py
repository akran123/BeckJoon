import sys
input = sys.stdin.readline

H, W = map(int, input().split())
grid = []
start_pos = None

for r in range(H):
    row = list(map(int, input().split()))
    grid.append(row)
    for c in range(len(row)):
        if row[c] == 9:
            start_pos = (r, c)

if start_pos:
    stack = [(start_pos[0], start_pos[1], d) for d in ['l', 'r', 'u', 'd']]
    visited_with_dir = set()
    visited_coords = {start_pos}

    while stack:
        r, c, d = stack.pop()
        
        if (r, c, d) in visited_with_dir:
            continue
        visited_with_dir.add((r, c, d))
        visited_coords.add((r, c))
        
        nr, nc = r, c
        if d == 'l': nc -= 1
        elif d == 'r': nc += 1
        elif d == 'u': nr -= 1
        elif d == 'd': nr += 1
        
        if 0 <= nr < H and 0 <= nc < W:
            cell = grid[nr][nc]
            next_d = d
            visited_coords.add((nr, nc))
            
            if cell == 0:
                pass
            elif cell == 1:
                if d in ['u', 'd']: continue 
            elif cell == 2:
                if d in ['l', 'r']: continue 
            elif cell == 3:
                if d == 'l': next_d = 'd'
                elif d == 'r': next_d = 'u'
                elif d == 'u': next_d = 'r'
                elif d == 'd': next_d = 'l'
            elif cell == 4:
                if d == 'l': next_d = 'u'
                elif d == 'r': next_d = 'd'
                elif d == 'u': next_d = 'l'
                elif d == 'd': next_d = 'r'
                
            stack.append((nr, nc, next_d))

    print(len(visited_coords))
else:
    print(0)