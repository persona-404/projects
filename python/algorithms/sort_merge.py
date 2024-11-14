list = [6, 3, 4, 1, 5, 2, 7, 0]
print ("unsorted", list)

def sort(list):
    if len(list) == 1:
        return list

    middle = int(len(list)/2)

    left = sort(list[0:middle]) 
    right = sort(list[middle:])
        
    return merge(left, right)

def merge(list1, list2):
    print ("list1", list1, "- list2", list2)
    
    sorted_list = []
    for i in range(0, len(list1)):
        if list1[i] > list2[i]:
            sorted_list.extend([list2[i], list1[i]])
        else:
            sorted_list.extend([list1[i], list2[i]])
    
    print ("sorted_list",sorted_list)
    return sorted_list

print ("sorted",sort(list))