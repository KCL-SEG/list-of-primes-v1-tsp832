"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 2
    while (len(list)) != number_of_primes:
        if isPrime(count):
            list.append(count)
        count +=1
    return list


def isPrime(n):
    if (n == 2 or n == 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False
    
    for i in range(5, i*i<n, 6):
        if (n % i == 0 or n % (i + 2) == 0):
            return False

    return True
