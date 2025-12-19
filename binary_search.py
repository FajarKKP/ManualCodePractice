def binary_search():
    sentences = ["apple", "banana", "cat", "fish", "giraffe"]
    target = "cat"
    left = 0
    right = len(sentences) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        if sentences[midpoint] == target:
            return midpoint
        elif target < sentences[midpoint]:
            right = midpoint - 1
        elif target > sentences[midpoint]:
            left = midpoint + 1
    return -1

print(binary_search())

