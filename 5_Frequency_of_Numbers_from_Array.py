def countOccurence(n, m):
    # code here
    freq = {}
    for i in m:
        count = 0
        for j in n:
            if i == j:
                count += 1
        freq[i] = count
    return freq

n = (1, 1, 1, 2, 2, 3, 4, 5, 7, 7, 8, 8, 8, 8, 10, 10)
m = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(countOccurence(n, m))

# Time Complexity: O(n + m)
# Space Complexity: O(m)
# where n is the length of the first array and m is the length of the second array