closing = {
    "]": "[",
    ")": "(",
    "}": "{",
    ">": "<",
}

scores = {
    "]": 57,
    ")": 3,
    "}": 1197,
    ">": 25137,
}

with open("input") as f:
    input = f.readlines()

score = 0
for line in input:
    line = line.strip()

    opened = []
    for c in line:
        if c in closing.values():
            opened.append(c)
        elif c in closing:
            if opened.pop() != closing[c]:
                score += scores[c]
                break

print("total =", score)
