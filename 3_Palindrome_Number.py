def palindromeNumber(num):
    n = num
    rev = 0
    if num < 0:
        return False
    while num != 0:
        rem  = num % 10
        rev = (rev * 10) + rem
        num = num // 10
    if n == rev:
        return True
    else:
        return False
    
n = input("Enter a number: ")
print("Is it a palindrome number: ", palindromeNumber(int(n)))

#time complexity = O(log10(n))
#space complexity = O(1)