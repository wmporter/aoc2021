def add_line(diagram, line):
    for pt in line:
        if diagram[pt[0]][pt[1]]:
            diagram[pt[0]][pt[1]] += 1
        else:
            diagram[pt[0]][pt[1]] = 1

def get_line(x1, y1, x2, y2):
    line = []
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            line.append((x1, y))
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            line.append((x, y1))
    return line

diagram = []
for i in range(1000):
    diagram.append([0] * 1000)

with open("input") as f:
    input = f.readlines()

for pts in input:
    pt1, pt2 = pts.split("->")
    x1, y1 = map(int, pt1.strip().split(","))
    x2, y2 = map(int, pt2.strip().split(","))
    line = get_line(x1, y1, x2, y2)
    if line:
        add_line(diagram, line)

print("total =", sum([v > 1 for r in diagram for v in r]))
