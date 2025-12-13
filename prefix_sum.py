def prefix_sum():
    nums = [1,2,5,7]
    new_nums = []
    sum_prev_element = 0

    for i in nums:
        sum_prev_element += i
        new_nums.append(sum_prev_element)
    
    return new_nums

print(prefix_sum())