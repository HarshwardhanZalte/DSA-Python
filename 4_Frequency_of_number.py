def findFrequency(arr, x):
    # code here
    count = 0
    for i in arr:
        if x == i:
            count += 1
    return count


arr = [1, 5, 3, 4, 5, 6, 7, 5, 9, 10]
x = 5
print(findFrequency(arr, x))

# Time Complexity: O(n) where n is the number of elements in the array
# Space Complexity: O(1) as we are using a constant amount of space