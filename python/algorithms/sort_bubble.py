list = [7, 2, 5, 4, 1, 6, 0, 3]
print ("unsorted",list)

def sort(list):
    n = len(list) - 1
    while (n):
        swap = False
        print("range:", range(0,n))
        for i in range(0, n): #range will go from 0 to the stop-1: in this case, 0 to n-1 (it wont go into list[n])
            print("i:",i," - i+1:", (i+1))
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                swap = True
        n = n-1
        
        if not swap:
            return list
    
    return list

print ("sorted:",sort(list))
