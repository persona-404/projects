# find the max value in array
# approach: 
#    initialize to -inifity 
#    check against each number of array
# complexity:
#    n = array len
#    time: O(n) => takes n steps to find the max value given that we have to check against all the elements in array
#    sapce: O(1) => we have one constant storing the max val - no scaler structures

def max_value(nums):
    max_value = float('-inf')
    for num in nums: # loop through the array
        if num > max_value:
            max_value = num

    return max_value

print (max_value([-5, -2, -1, -11]))