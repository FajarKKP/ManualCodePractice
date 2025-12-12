# Brute force
def two_sum():
    arr_list = [2, 7, 11, 5]
    target = 9
    output = []

    for element in range(len(arr_list)):
        temp_var = target - arr_list[element]

        for next_element in range(element +1, len(arr_list)):
            if temp_var == arr_list[next_element]:
                output = [element, next_element]
                break
    
    return output 

print(two_sum())

# Hash map
def two_sum_hm():
    arr_list = [2, 7, 11, 5]
    target = 9
    seen = {}


    for i, num in enumerate(arr_list):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return seen

print(two_sum_hm())