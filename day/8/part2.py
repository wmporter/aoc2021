# This solution uses sets as a way of comparing
# the segments to each other because the ordering of 
# the segments does not matter. The number 1 can be
# "cf" or "fc"

# Real values
original = list(map(set, [
    "abcefg", "cf", "acdeg", "acdfg", "bcdf",
    "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"
]))

# The "special" numbers are 1, 4, 7, and 8 because
# they have a unique number of segments
# There are three numbers that have 5 segments (2, 3, 5)
# and three with 6 segments (0, 6, 9)
# We don't know which is which yet but it's useful to have
# them grouped together, so we return them as well
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

    # We can calculate the sets for 3 and 9 right away 
    # using set difference (conveniently usable with the - operator)
    # As a refresher, left - right evalutes to a set that contains everything
    # from the left set with all items it has in common with the right set 
    # removed
    #
    # Of the 5-segment numbers, 3 is the only one that contains
    # every segment from 7, so 7 - 3 is the only result that will be empty
    #
    # Similar strategy for 9 since it's the only one of the 6-segment
    # numbers that contains all of 4's segments
    three = [f for f in fives if not seven - f][0]
    nine = [s for s in sixes if not four - s][0]

    # Here we calculate the sets for each individual segment
    # These are all sets with a single item in them, which is 
    # why we have to use .pop() later to extract the item when 
    # setting up the mapping
    
    # Pretty easy, take the segments from 7 remove the ones from
    # 1 and you're left with the top segment
    top = seven - one

    # Same logic here. The bottom left segment is the only one not
    # in common between 8 and 9
    bot_left = eight - nine

    # nine - four leaves us with two segments, top and bottom. But
    # which is which? Well since we already know what top is, just 
    # remove that one as well
    bot = nine - four - top

    # Similarly three - seven leaves the middle and bottom segments
    # so we just have to remove the bottom one to find the middle
    mid = three - seven - bot
    
    # And we do the same thing yet again here. four - one leaves
    # the middle and top left segments, so remove the middle too
    top_left = four - one - mid

    # The only full numbers we've calculated so far (1, 3, 4, 7, 8, 9)
    # all contain the top right and bottom right segments, so we can't 
    # really manipulate any of them to look for these last two segments.
    # What we have to do is look for numbers we haven't calculated yet
    # (0, 2, 5, 6) and see which ones we can use. Both 2 and 5 are in the 
    # fives list, but since 2 is missing bottom right and 5 is missing 
    # top right, if we do one - n with the fives list, we'll end up with 
    # two results and still won't know which is which. However, 6 is also
    # missing top right and the other items in the sixes list (0 and 9) 
    # aren't missing either segment from 1, so we should get just one result
    # where there's a left over segment if we do one - n.
    top_right = [one - n for n in sixes if one - n][0]

    # Now that we have top right, getting bottom right is easy
    bot_right = one - top_right

    # Now that we have all seven segments, we can map to the original
    # segments
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

        # Grab each segment from the current digit and re-create what the digit 
        # would be if things weren't scrambled
        orig_value = set(''.join([new_mapping[d] for d in digit]))
        
        # Use the correct set of segments to look up its value 
        # and append it to the the value we have so far
        value = value * 10 + original.index(orig_value)
    
    count += value

print("total =", count)
