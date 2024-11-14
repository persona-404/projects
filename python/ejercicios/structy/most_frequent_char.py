"""
    Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.
    
    If a letter appears the same amount of times, return the first ocurrance
    
    Returns:
        str: char that appears the most
"""

from collections import Counter

# using collections
def most_frequent_char(str):
    common = Counter(str).most_common(1)
    return common[0][0]

# manually - runs O(n) and uses n space - linear time, linear space
def most_freq_char(str):
    char_count = {}
    for char in str:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

        #print (char, char_count[char], most_chars, most_char)
        #if char_count[char] > most_chars:
        #    most_char = char
        #    most_chars = char_count[char]

    most_chars = 0
    most_char = ''
    for char, count in char_count.items():
        if count > most_chars:
            most_char = char
            most_chars = count

    # another way:
    # most_char = None
    # for char in str:
    #    if best is None or char_count[char] > char_count[most_char]
    #       most_char = char
    # return most_char

    return most_char

    
print (most_freq_char('mississippi'))
#print (most_frequent_char('mississippi'))