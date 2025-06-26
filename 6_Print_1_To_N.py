def printNos(n):
    #Code here
    if n==0:
        return
    printNos(n-1)
    print(n,end=" ")

n = int(input("Enter a number: "))
printNos(n)