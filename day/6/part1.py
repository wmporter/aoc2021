with open("input") as f:
    input = f.readline()

fish = list(map(int, input.strip().split(",")))

for day in range(80):
    newfish = []
    for i, f in enumerate(fish):
        if f == 0:
            fish[i] = 6
            newfish.append(8)
        else:
            fish[i] -= 1
    fish.extend(newfish)


print("total =", len(fish))
