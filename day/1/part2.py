increases = 0
with open("input") as f:
    inputs = [int(s.strip()) for s in f.readlines()]
    first = 0
    last = 3
    prev = sum(inputs[first:last])
    while last <= len(inputs):
        first += 1
        last += 1
        next = sum(inputs[first:last])
        if next > prev:
            increases += 1
        prev = next

print(f"{increases=}")
