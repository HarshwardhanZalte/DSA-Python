def frequencyMap(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

arr = [1, 5, 3, 4, 5, 6, 7, 5, 9, 10]
print(frequencyMap(arr))

# Time Complexity: O(n) where n is the number of elements in the array
# Space Complexity: O(n) as we are using a dictionary to store the frequency of each element