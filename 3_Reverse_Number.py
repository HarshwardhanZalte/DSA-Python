def reverserNumber(num):
    rev = 0
    while num != 0:
        rem = num % 10
        rev = (rev * 10) + rem
        num = num // 10
    return rev

n = input("Enter a number to reverser: ")
print("Reverser number is: ", reverserNumber(int(n)))

# Time Complexity: O(d) where d is the number of digits in the number
# Space Complexity: O(1) as we are using a constant amount of space