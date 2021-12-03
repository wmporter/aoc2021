# Wrap all this in a function so it can be called with different inputs
def count_bits(inputs):
    ones_count = [0] * 12
    zero_count = [0] * 12
    for line in inputs:
        for i, bit in enumerate(line):
            if bit == '1': ones_count[i] += 1
            else: zero_count[i] += 1

    gamma = ['0'] * 12
    epsilon = ['0'] * 12

    for i in range(12):
        if ones_count[i] >= zero_count[i]:
            gamma[i] = '1'
        else:
            epsilon[i] = '1'

    return gamma, epsilon

# Quick filter function
def filter(f, arr):
    newarr = []
    for a in arr:
        if f(a): newarr.append(a)
    return newarr

with open("input") as f:
    inputs = [input.strip() for input in f.readlines()]

gamma_inp = inputs
epsilon_inp = inputs
for i in range(12):
    # Important step: recount everything each time through the loop
    gamma, _ = count_bits(gamma_inp)
    _, epsilon = count_bits(epsilon_inp)

    if len(gamma_inp) > 1:
        gamma_inp = filter(lambda x: x[i] == gamma[i], gamma_inp)
    if len(epsilon_inp) > 1:
        epsilon_inp = filter(lambda x: x[i] == epsilon[i], epsilon_inp)

    if len(gamma_inp) == 1 and len(epsilon_inp) == 1:
        break
    

print("total =", int(gamma_inp[0], 2) * int(epsilon_inp[0], 2))
