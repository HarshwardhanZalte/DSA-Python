def countNumber(num):
    count = 0
    while num != 0:
        num = num // 10
        count += 1
    return count     # int(log10(n) + 1)

n = input("Enter a number: ")
print("Number of digits is: ", countNumber(int(n)))


#time complexity = O(log10(n))
#space complexity = O(1)