def check_palindrome():
    sentences = "kayak"
    pointer_left = 0
    pointer_right = len(sentences) - 1

    while pointer_left < pointer_right:
        if sentences[pointer_left] != sentences[pointer_right]:
            return False
        pointer_left += 1
        pointer_right -= 1

    return True
    
print(check_palindrome())