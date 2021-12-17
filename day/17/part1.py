def within_target(loc):
    x, y = loc
    return minx <= x <= maxx and miny <= y <= maxy

def too_deep(loc):
    x, y = loc
    return x > maxx

def too_short(loc):
    x, y = loc
    return x < minx and y < miny

def too_high(loc):
    x, y = loc
    return y < miny

def shoot(xvel, yvel):
    x = y = 0
    max_height = -1
    while True:
        x += xvel
        y += yvel
        if y > max_height:
            max_height = y
        if within_target((x, y)):
            return max_height
        if too_high((x, y)) or too_deep((x, y)):
            return False
        if xvel > 0: xvel -= 1
        elif xvel < 0: xvel += 1
        yvel -= 1

with open("input") as f:
    inp = f.readline()

left, right = inp.strip().split(',')
minx, maxx = left.split('=')[1].split('..')
miny, maxy = right.split('=')[1].split('..')
minx = int(minx)
miny = int(miny)
maxx = int(maxx)
maxy = int(maxy)

xvel = yvel = 1
max_height = -9999
for x in range(100):
    for y in range(-100,100):
        height = shoot(xvel+x, yvel+y)
        if height and height > max_height:
            max_height = height

print("total =", max_height)
