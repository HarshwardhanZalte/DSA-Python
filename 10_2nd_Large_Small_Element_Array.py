def getSecondOrderElements(n, a):
    # Write your code here.
    a.sort()
    del a[len(a)-1]
    return [a[len(a)-1], a[1]]


n = int(input())
a = list(map(int, input().split()))
print(getSecondOrderElements(n, a))