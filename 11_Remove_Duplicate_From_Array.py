def removeDupliacate(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return arr
    unique_arr = []
    unique_arr.append(arr[0])
    for i in range(1, n):
        if arr[i] not in unique_arr:
            unique_arr.append(arr[i])
    return unique_arr


arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(removeDupliacate(arr))

# Time Complexity: O(n)
# Space Complexity: O(n)