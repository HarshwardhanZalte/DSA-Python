def largestElement(arr):
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

    # return max(arr)

arr = [3, 1, -4, 1, 5, -9, 2, 6, -5, 3, 7]
print(largestElement(arr))

# Time Complexity: O(n)
# Space Complexity: O(1)