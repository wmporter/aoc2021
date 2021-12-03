gamma = ['0'] * 12
epsilon = ['0'] * 12
ones_count = [0] * 12
zero_count = [0] * 12

with open("input") as f:
    inputs = [input.strip() for input in f.readlines()]

for line in inputs:
    for i, bit in enumerate(line):
        if bit == '1': ones_count[i] += 1
        else: zero_count[i] += 1

for i in range(12):
    if ones_count[i] >= zero_count[i]:
        gamma[i] = '1'
    else:
        epsilon[i] = '1'

def filter(f, arr):
    newarr = []
    for a in arr:
        if f(a): newarr.append(a)
    return newarr

i = 0
inp = inputs[:]
inp2 = inputs[:]
while len(inp) > 1 or len(inp2) > 1:
    if len(inp) > 1:
        inp = filter(lambda x: x[i] == gamma[i], inp)
    if len(inp2) > 1:
        inp2 = filter(lambda x: x[i] == epsilon[i], inp2)

    i += 1

print("gamma", ''.join(gamma))
print("epsilon", ''.join(epsilon))
print("inp:", inp)
print("inp2:", inp2)
print("total =", int(inp[0], 2) * int(inp2[0], 2))
