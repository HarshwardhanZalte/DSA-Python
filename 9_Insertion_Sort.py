def insertionSort(num):
    n = len(num)
    for i in range(1,n):
        key = num[i]
        j = i - 1
        while j >= 0 and num[j] > key:
            num[j+1] = num[j]
            j -= 1
        num[j+1] = key
    return num

n = [64, 34, 25, 12, 22, 11, 90]
print(insertionSort(n))

# Time Complexity: O(n^2)
# Space Complexity: O(1)