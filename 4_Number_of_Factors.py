def countFactors (n):
    # code here
    num = []
    for i in range(1, n+1):
        if n % i == 0:
            num.append(i)
    print(num)
    return len(num)


n = int(input("Enter Number:"))
print("Number of factors:",countFactors(n))

# Time Complexity: O(n) where n is the number of factors of the number
# Space Complexity: O(n) as we are storing the factors in