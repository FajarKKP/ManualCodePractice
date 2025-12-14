def reverse_array():
    ori_array = [1, 3, 4, 5, 7]
    pointer_left = 0
    pointer_right = len(ori_array) - 1


    for i in range(len(ori_array)):
        if pointer_left < pointer_right:
            temp = ori_array[pointer_left]
            ori_array[pointer_left] = ori_array[pointer_right]
            ori_array[pointer_right] = temp

            pointer_right -= 1
            pointer_left += 1
    
    return ori_array
    
print(reverse_array())