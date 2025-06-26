def printNos(n):
    # Code here
    if n == 0:
        return
    print(n, end=" ")
    printNos(n-1)


n = int(input("Enter a number: "))
printNos(n)