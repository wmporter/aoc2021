with open("input") as f:
    inp = f.readlines()

# A set of all individual letters and all the 2-letter pairs
letter_combos = set()
pair_maps = {}
for pair_map in inp[2:]:
    pair, insert = pair_map.strip().split(' -> ')
    letter_combos |= {pair, pair[0], pair[1]}
    pair_maps[pair] = insert

counts = {}
for l in letter_combos:
    counts[l] = 0

# Initalize the counts based on the first line of input.
# This is how we're going to keep track of the new polymer at each stage. 
# We can't brute force this the way we were able to do in part 1 because 
# the string size essentially doubles on each iteration. 10 iterations means 
# your string is a couple thousand characters long at the end. But 40 
# iterations means your string ends up a few TRILLION characters long, which 
# is not only probably too large for your computer to handle, but will take 
# too long even if it could. 10 iterations takes about 15 milliseconds. 20
# takes 15 seconds. Each increase of 10 iterations is a thousand-fold increase
# in time. So 30 iterations would take more than 4 hours and 40 iterations would
# take more than 5 months. So we can't use the same approach. Rather than 
# iterate through a string that grows exponentially, we keep track of the count of each 
# overlapping pair the string contains. These counts will get big but the 
# computer can handle big numbers. The size of the data structure stays really
# small. Only enough memory needed to hold all the single letters and their
# 2-letter permutations (N + N^2) plus their large counts.
polymer = inp[0].strip()
for i in range(len(polymer)):
    if i < len(polymer) - 1:
        pair = polymer[i:i+2]
        counts[pair] += 1
    counts[polymer[i]] += 1

for _ in range(40):
    # Each pair results in two new pairs being added to the polymer
    # on the next step
    # For example, CB becomes CH and HB (from CHB)
    # This means two things: 
    # 1) However many CBs there are, you will get the same number of CH and HB pairs
    #    This is the reason we do += counts[pair]
    # 2) All the CBs are gone now, at least the ones that already existed
    #    This is why we initialize new_counts to be zeroes
    new_counts = {k:0 for k in counts if len(k) == 2}
    for pair, insert in pair_maps.items():
        left, right = pair
        counts[insert] += counts[pair]
        new_counts[left+insert] += counts[pair]
        new_counts[insert+right] += counts[pair]
    counts.update(new_counts)
    
singles = [v for k,v in counts.items() if len(k) == 1]
print("total =", max(singles)-min(singles))
