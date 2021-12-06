DAYS = 256

with open("input") as f:
    input = f.readline()

fish = list(map(int, input.strip().split(",")))
fish_added = [0] * DAYS

for f in fish:
    fish_added[f] += 1
    for i in range(f+7, DAYS, 7):
        fish_added[i] += 1

for day in range(DAYS):
    for d in range(day+9, DAYS, 7):
        fish_added[d] += fish_added[day]

print("total =", sum(fish_added)+len(fish))
