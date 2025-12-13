def unique_char():
    words = "labmoogiini"
    output = 0
    seen = {}

    # Two steps to solve, first to count the number. Then two check the fist one where it is not a repetition
    for char in (words):
        seen[char] = seen.get(char, 0) + 1

    # check the letter where it is 1. It means that that letter is not a repetition
    for i, char in enumerate(words):
        if seen[char] == 1:
            return i
    return -1

print(unique_char())
