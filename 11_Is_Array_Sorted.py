def isSorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

arr = [1, 2, 3, 4, 5]
print(isSorted(arr))

arr = [1, 3, 5, 2, 7, 5]
print(isSorted(arr))

# Time Complexity: O(n)
# Space Complexity: O(1)