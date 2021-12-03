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
    if ones_count[i] > zero_count[i]:
        gamma[i] = '1'
    else:
        epsilon[i] = '1'

gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)

print("total =", gamma * epsilon)
