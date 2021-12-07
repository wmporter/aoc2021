def averages(values):
    s = sum(values)
    mean = s // len(values)
    values.sort()
    mid = len(values) // 2
    if len(values) % 2:
        median = values[mid]
    else:
        median = sum(values[mid-1:mid+1]) // 2
    occurs = {}
    mode, mode_amt = -1, 0
    for v in values:
        amt = occurs.get(v, 0) + 1
        if amt > mode_amt:
            mode = v
            mode_amt = amt
        occurs[v] = amt
    return mean, median, mode

def distance(values, pos):
    return sum([abs(pos-v) for v in values])

with open("input") as f:
    input = list(map(int, f.readline().strip().split(",")))

mean, median, mode = averages(input)
print("total =", min(map(lambda x: distance(input, x), (mean, median, mode))))
