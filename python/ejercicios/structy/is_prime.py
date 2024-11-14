# return a boolean indicating whether or not the given number is prime
# consider: we know that 1 & n are divisible by n so we can skip them
#           any other number we find divides our n, it would mean that this number n is prime
#           0/1 is not a prime
# complexity:
#    n = ainput number
#    time: O(sqrt(n)) => takes n-1 steps to find how many  numbers are divisible by n (2 to n-1)
#    sapce: O(1) => we have one constant storing - no scaler structures
#
# theory (and to make it better complexity):
#    The property of being prime is called primality. A simple but slow method of checking the primality of a 
#    given number called trial division, tests whether is a multiple of any integer between 2 and sqrt(n)
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
  
    dividends = 0
    for i in range(2,int(sqrt(n) + 1)): # make it inclusive because we still need to check the sqrt number 
        if (n % i == 0):
            return False

    return True

print("0",is_prime(0))
print("2",is_prime(2))
print("3",is_prime(3))
print("4",is_prime(4))
print("5",is_prime(5))
print("6",is_prime(6))
print("7",is_prime(7))
print("8",is_prime(8))
print("25",is_prime(25))
print("31",is_prime(31))
print("2017",is_prime(2017))
print("2048",is_prime(2048))
print("1",is_prime(1))
print("713",is_prime(713))