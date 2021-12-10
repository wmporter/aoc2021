closing = {
    "]": "[",
    ")": "(",
    "}": "{",
    ">": "<",
}
opening = {v:k for k,v in closing.items()}

scores = {
    "]": 2,
    ")": 1,
    "}": 3,
    ">": 4,
}

with open("input") as f:
    input = f.readlines()

score_list = []
for line in input:
    line = line.strip()

    opened = []
    corrupted = False
    for c in line:
        if c in opening:
            opened.append(c)
        elif c in closing:
            if opened.pop() != closing[c]:
                corrupted = True
                break
        
    if corrupted:
        continue
    
    score = 0
    for c in opened[::-1]:
        score = score * 5 + scores[opening[c]]
    score_list.append(score)

score_list.sort()
print("total =", score_list[len(score_list)//2])
