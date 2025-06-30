def printNos(n):
    #Code here
    if n==0:
        return
    printNos(n-1)
    print(n,end=" ")

n = int(input("Enter a number: "))
printNos(n)

# Time Complexity: O(n)
# Space Complexity: O(n)