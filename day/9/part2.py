def neighbors(heights, x, y):
    maxx = len(heights) - 1
    maxy = len(heights[0]) - 1
    ret = []
    if x > 0:
        ret.append((x-1, y))
    if x < maxx:
        ret.append((x+1, y))
    if y > 0:
        ret.append((x, y-1))
    if y < maxy:
        ret.append((x, y+1))
    return ret

def minimal(heights, x, y):
    current = heights[x][y]
    for w, z in neighbors(heights, x, y):
        if heights[w][z] <= current:
            return False
    return True

def basin(heights, x, y):
    n = {(x, y)}
    process = {(x, y)}
    while len(process):
        x, y = process.pop()
        if heights[x][y] != 9:
            n.add((x, y))
            process = process | (set(neighbors(heights, x, y)) - n)

    return len(n)

def max_basins(basins, basin):
    if basin > basins[2]:
        basins.append(basin)
        basins.pop(0)
    elif basin > basins[1]:
        basins[0] = basins[1]
        basins[1] = basin
    elif basin > basins[0]:
        basins[0] = basin

with open("input") as f:
    input = f.readlines()

for i in range(len(input)):
    input[i] = list(map(int, list(input[i].strip())))

basins = [-1, -1, -1]
for i in range(len(input)):
    for j in range(len(input[0])):
        if minimal(input, i, j):
            max_basins(basins, basin(input, i, j))

print("total =", basins[0]*basins[1]*basins[2])
