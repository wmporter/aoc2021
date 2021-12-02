pos = {
    "horiz": 0,
    "depth": 0,
}
movement = {
    "forward": lambda x: pos.update({"horiz": pos["horiz"] + x}),
    "down": lambda x: pos.update({"depth": pos["depth"] + x}),
    "up": lambda x: pos.update({"depth": pos["depth"] - x}),
}
with open("input") as f:
    inputs = [input.strip() for input in f.readlines()]
    for line in inputs:
        d, amt = line.split()
        movement[d](int(amt))

print("total =", pos["horiz"] * pos["depth"])
