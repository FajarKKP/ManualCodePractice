def sliding_window():
    current_string = "tmmzuxt"
    stored_kvp = {}
    max_window_len = 0
    left_pointer = 0
    
    for i, char in enumerate(current_string):
        if char in stored_kvp and stored_kvp[char] >= left_pointer:
            left_pointer = stored_kvp[char] + 1
        else:
            stored_kvp[char] = i
            max_window_len = max(left_pointer, i - left_pointer + 1) 
    return max_window_len

print(sliding_window())
