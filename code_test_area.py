def testing():
    nums = [2,4,1,6,8,1,4,6]
    k = 3
    output = 0
    window = []

    for num in nums:
        window.append(num)

        if len(window) == k:
            window_sum = sum(window)
            output = max(output, window_sum)
            window.pop(0)
            
    return output
        
print(testing())