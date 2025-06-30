def sumOfSeries(n):
    #code here
    if n == 1:
        return 1
    sum = sumOfSeries(n-1)
    sum += n**3
    return sum

n = int(input("Enter a number: "))
print("Sum of series is: ", sumOfSeries(n))

# Time Complexity: O(n)
# Space Complexity: O(n)