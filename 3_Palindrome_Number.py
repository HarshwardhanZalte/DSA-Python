def palindromeNumber(n):
    original = n
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    
    return original == reversed_num
    
n = input("Enter a number: ")
print("Is it a palindrome number: ", palindromeNumber(int(n)))

#time complexity = O(log10(n))
#space complexity = O(1)