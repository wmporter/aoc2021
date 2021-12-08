def count_special(segments):
    special = [2,3,4,7]
    return sum([1 for s in segments if len(s) in special])

with open("input") as f:
    input = f.readlines()

count = 0
for line in input:
    _, digits = line.strip().split("|")

    digits = digits.split()
    count += count_special(digits)

print("total =", count)
