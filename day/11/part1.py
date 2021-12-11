def neighbors(grid, x, y):
    maxx = len(grid) - 1
    maxy = len(grid[0]) - 1
    ret = []
    if x > 0:
        ret.append((x-1, y))
        if y > 0:
            ret.append((x-1, y-1))
        if y < maxy:
            ret.append((x-1, y+1))
    if x < maxx:
        ret.append((x+1, y))
        if y < maxy:
            ret.append((x+1, y+1))
        if y > 0:
            ret.append((x+1, y-1))
    if y > 0:
        ret.append((x, y-1))
    if y < maxy:
        ret.append((x, y+1))
    return ret

with open("input") as f:
    inp = f.readlines()

grid = []
for i in inp:
    grid.append(list(map(int, [d for d in i.strip()])))

total = 0
for step in range(100):
    
    for r in range(10):
        for c in range(10):
            grid[r][c] += 1
    
    flashed = set()
    queue = set()
    for r in range(10):
        for c in range(10):
            if grid[r][c] > 9:
                queue.add((r,c))
                queue -= flashed
                while queue:
                    qr, qc = queue.pop()
                    flashed.add((qr, qc))
                    
                    for n in neighbors(grid, qr, qc):
                        nr, nc = n
                        grid[nr][nc] += 1
                        if grid[nr][nc] > 9:
                            queue.add((nr,nc))
                    queue -= flashed

    total += len(flashed)
    for r,c in flashed:
        grid[r][c] = 0

print("total =", total)
