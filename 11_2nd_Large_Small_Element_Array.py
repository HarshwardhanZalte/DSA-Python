def getSecondOrderElements(n, a):
    # Write your code here.
    a.sort()
    return [a[len(a)-2], a[1]]

def largest(arr):
    largest = arr[0]
    s_largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
        elif arr[i] > s_largest and arr[i] < largest:
            s_largest = arr[i]
    return s_largest

n = int(input())
a = list(map(int, input().split()))
print(getSecondOrderElements(n, a))
print(a)

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

