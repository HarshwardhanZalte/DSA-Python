def armstrongNumber(num):
    n = num
    sum = 0
    count = 0
    while n != 0:
        n = n // 10
        count += 1
    n = num
    while n != 0:
        rem = n % 10
        sum = sum + (rem ** count)
        n = n // 10
    if num == sum:
        return True
    else:
        return False

n = input("Enter a number: ")
print("Is it an Armstrong number: ", armstrongNumber(int(n)))

# Time Complexity: O(d) where d is the number of digits in the number
# Space Complexity: O(1) as we are using a constant amount of space