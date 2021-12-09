def neighbors(heights, x, y):
    maxx = len(heights) - 1
    maxy = len(heights[0]) - 1
    ret = []
    if x > 0:
        ret.append(heights[x-1][y])
    if x < maxx:
        ret.append(heights[x+1][y])
    if y > 0:
        ret.append(heights[x][y-1])
    if y < maxy:
        ret.append(heights[x][y+1])
    return ret

def minimal(heights, x, y):
    current = heights[x][y]
    for n in neighbors(heights, x, y):
        if n <= current:
            return False
    return True

with open("input") as f:
    input = f.readlines()

for i in range(len(input)):
    input[i] = list(map(int, list(input[i].strip())))

total_risk = 0
for i in range(len(input)):
    for j in range(len(input[0])):
        if minimal(input, i, j):
            # print(i, j)
            total_risk += input[i][j] + 1

print("total =", total_risk)
