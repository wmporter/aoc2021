def neighbors(loc, grid):
    x, y = loc
    maxx = len(grid) - 1
    maxy = len(grid[0]) - 1

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

def next_visit(visited):
    n = None
    for loc, val in visited.items():
        if val[0] == 0:
            if n is None or val[1] < minimum:
                n = loc
                minimum = val[1]
    return n

with open("input") as f:
    inp = f.readlines()

maze = []
for row in inp:
    maze.append([int(d) for d in row.strip()])

visited = {(0,0): [0,0]}
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if i == 0 and j == 0:
            continue
        visited[(i,j)] = [0, 1000000]

end = (len(maze)-1, len(maze[0])-1)

found = False
for _ in range(len(visited)):
    nv = next_visit(visited)
    if nv == end:
        break
    for n in neighbors(nv, maze):
        i,j = n
        if visited[n][0] == 0:
            old = visited[nv][1]
            dist = old + maze[i][j]
            if visited[n][1] > dist:
                visited[n][1] = dist
    visited[nv][0] = 1

print("total =", visited[end][1])
