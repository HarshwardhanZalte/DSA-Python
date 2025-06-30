from math import sqrt

def isPrime(n):
    # code here
    if n<=1:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
print("Is it a prime number: ", isPrime(n))

# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)