# Real values
original = list(map(set, [
    "abcefg", "cf", "acdeg", "acdfg", "bcdf",
    "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"
]))

def get_special(segments):
    fives = []
    sixes = []
    for s in segments:
        if len(s) == 2:
            one = set(s)
        elif len(s) == 3:
            seven = set(s)
        elif len(s) == 4:
            four = set(s)
        elif len(s) == 5:
            fives.append(set(s))
        elif len(s) == 6:
            sixes.append(set(s))
        elif len(s) == 7:
            eight = set(s)
    return [one, four, seven, eight] + fives + sixes

with open("input") as f:
    input = f.readlines()

count = 0
for line in input:
    segments, digits = line.strip().split("|")
    segments = segments.split()

    one, four, seven, eight, *rest = get_special(segments)
    fives = rest[:3]
    sixes = rest[3:]

    three = [f for f in fives if not seven - f][0]
    nine = [s for s in sixes if not four - s][0]

    top = seven - one
    bot_left = eight - nine
    top_right = [one - n for n in sixes if one - n][0]
    bot_right = one - top_right
    bot = nine - four - top
    mid = three - seven - bot
    top_left = four - (one | mid)

    new_mapping = {
        top.pop(): 'a',
        top_left.pop(): 'b',
        top_right.pop(): 'c',
        mid.pop(): 'd',
        bot_left.pop(): 'e',
        bot_right.pop(): 'f',
        bot.pop(): 'g',
    }

    digits = digits.split()
    value = 0
    for i in range(4):
        digit = digits[i]
        orig_value = set(''.join([new_mapping[d] for d in digit]))
        value = value * 10 + original.index(orig_value)
    count += value

print("total =", count)
