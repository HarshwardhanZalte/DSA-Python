def findLucky(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    lucky = -1
    for num, count in freq.items():
        if num == count:
            lucky = max(lucky, num)
    return lucky


arr = [1, 2, 2, 3, 3, 3]
print(findLucky(arr))