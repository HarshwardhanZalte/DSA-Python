def printHello(n):
    # Code here
    if n == 0:
        return
    printHello(n-1)
    print("Hello", end=" ")


n = int(input("Enter a number: "))
printHello(n)