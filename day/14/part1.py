with open("input") as f:
    inp = f.readlines()

pair_maps = {}
for pair_map in inp[2:]:
    pair, insert = pair_map.strip().split(' -> ')
    pair_maps[pair] = insert
    
polymer = inp[0].strip()
counts = {}
for c in polymer:
    if c not in counts:
        counts[c] = polymer.count(c)

for _ in range(10):
    new_polymer = ""
    for i in range(len(polymer)-1):
        left, right = polymer[i:i+2]
        insert = pair_maps[left+right]
        counts[insert] = counts.get(insert, 0) + 1
        new_polymer += left + insert
    polymer = new_polymer + right

print("total =", max(counts.values())-min(counts.values()))
