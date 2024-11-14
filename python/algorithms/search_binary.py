# binary search works when the list is sorted

list = [0, 1, 2, 3, 4, 5, 6, 7]
find = 4

def binary_search(list, num):
    if not list:
        return False;
    
    middle = int(len(list) / 2)

    if num == list[middle]:
        return True;
    elif num > list[middle]:
        return binary_search(list[-middle:], num)
    else:
        return binary_search(list[:middle], num)

if binary_search(list, 4):
    print("Number", find, "was found")