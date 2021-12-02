increases = 0
with open("input") as f:
    inputs = f.readlines()
    prev = int(inputs[0].strip())
    print(prev)
    for next in inputs[1:]:
        next = int(next.strip())
        if next > prev:
            increases += 1
            print(next, increases)
        else:
            print(next)
        prev = next

print(f"{increases=}")
