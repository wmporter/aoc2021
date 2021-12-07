def averages(values):
    res = set()

    # Mode
    occurs = {}
    for v in values:
        occurs.update({v: occurs.get(v, 0) + 1})
    res.add(max(occurs.items(), key=lambda x: x[1])[0])
    
    # Mean
    values_sum = sum(values)
    mean = values_sum // len(values)
    if mean != values_sum / len(values):
        res.add(int(values_sum / len(values) + 0.5))
    res.add(mean)

    # Median
    values.sort()
    mid = len(values) // 2
    if len(values) % 2:
        res.add(values[mid])
    else:
        res.add(sum(values[mid-1:mid+1]) // 2)
    
    return res

def distance(values, pos):
    return sum([abs(pos-v) for v in values])

with open("input") as f:
    input = list(map(int, f.readline().strip().split(",")))

print("total =", min(map(lambda x: distance(input, x), averages(input))))
