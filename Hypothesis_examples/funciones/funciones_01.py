
# Rosetta Code

# Task

# Given a string containing uppercase characters (A-Z), compress repeated
# 'runs' of the same character by storing the length of that run,
# and provide a function to reverse the compression.

# The output can be anything, as long as you can recreate the input with it.


# Example
#    Input: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
#    Output: 12W1B12W3B24W1B14W

def encode(input_string):
    count = 1
    prev = ""
    lst = []
    character = ""
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1  # Missing reset operation
            prev = character
        else:
            count += 1
    entry = (character, count)
    lst.append(entry)
    return lst


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q
