"""
    Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

    Be sure to return the indices, not the elements themselves.
    
    complexity:
        brute force: O(n^2) = we have 2 fors to iterate through the list to sum each element
        with dictionary (hash map): O(n)
"""

def pair_sum(numbers, target_sum):
    # brute force
    #for i in range(0,len(numbers)):
    #    for j in range(i+1, len(numbers)):
    #        if (numbers[i] + numbers[j]) == target_sum:
    #            return i,j
    
    # to avoid brute force:
    #   - save the numbers we have seen
    #   - iterate through the numbers
    #      - to help not iterate twice, save the remainder of the current value we are seeing
    #      - check if we have seen that "remainder" in the "previous numbers" and if so, we are done
    #        - if not, just add it to our seen numbers
    prev_numbers = {}
    for index, value in enumerate(numbers):
        remainder = target_sum - value
        
        if remainder in prev_numbers:
            return index, prev_numbers[remainder]
        
        prev_numbers[value] = index
            
print (pair_sum([3, 2, 5, 4, 1], 8))