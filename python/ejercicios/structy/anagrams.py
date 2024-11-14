"""
    Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

    For Counter, we would have O(n) for turning the string into dict
    Sorting might be faster operation but consider string sizes. Dict is good in short ones, and faster on larger ones
"""

from collections import Counter

def anagrams(s1, s2, v):
    if (v == 1):
        # one way is to make the strings a list, sort and then compare them
        return (sorted(list(s1)) == sorted(list(s2)))
    else:
        # another way could be creating a counter of both and then compare
        c1 = Counter(s1)
        c2 = Counter(s2)

        return (c1 == c2)

print (anagrams("paper", "reapa", 1))