def foldup(grid, y):
    try:
        for r in range(1, len(grid)-y):
            for c in range(len(grid[r])):

                if grid[y+r][c] == '#':
                    grid[y-r][c] = '#'
    except IndexError:
        print("row, col:", r, ",", c)
        raise
    grid = grid[:y]

def foldleft(grid, x):
    for r in range(len(grid)):
        for c in range(1, len(grid[r])-x):
            if grid[r][x+c] == '#':
                grid[r][x-c] = '#'

def count_dots(grid):
    count = 0
    for r in grid:
        for c in r:
            if c == "#":
                count += 1
    return count

def show_grid(grid):
    for r in grid:
        for c in r:
            print(c, end=' ')
        print()

with open("input") as f:
    inp = f.readlines()

dots = []
commands = []
maxx, maxy = 0, 0
for line in inp:
    line = line.strip()
    if line == "":
        continue

    if line.startswith("fold"):
        commands.append(line)
    else:
        c, r = line.split(",")
        maxx = max(int(c), maxx)
        maxy = max(int(r), maxy)
        dots.append((int(c), int(r)))

grid = []
for r in range(maxy+1):
    grid.append(['.'] * (maxx+1))
for c, r in dots:
    grid[r][c] = '#'

for command in commands[:1]:
    value = int(command.split('=')[1])
    if 'x=' in command:
        foldleft(grid, value)
        for r in range(len(grid)):
            grid[r] = grid[r][:value]
    else:
        foldup(grid, value)
        grid = grid[:value]

# show_grid(grid)
print("total =", count_dots(grid))
