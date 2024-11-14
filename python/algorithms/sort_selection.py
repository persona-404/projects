list = [7, 2, 5, 4, 1, 6, 0, 3]
print ("unsorted",list)

def sort(list):
    for i in range(len(list)):
        temp = list[i]
        j = i
        smallest_value = list[i]
        for j in range(i, len(list)):
            if list[j] < smallest_value:
                smallest_value = list[j]
                swap_index = j # need to know with what index we will swap
        
        # if the current value is bigger than the smallest we wound, lets swap
        if (temp > smallest_value):
            list[i] = smallest_value
            list[swap_index] = temp

    return list

print ("sorted",sort(list))

