def findUnion(a,b):
    n = len(a)
    m = len(b)
    res = []
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] <= b[j]:
            if len(res) == 0 or res[-1] != a[i]:
                res.append(a[i])
            i += 1
        else:
            if len(res) == 0 or res[-1] != b[j]:
                res.append(b[j])
            j += 1
    while i < n:
        if len(res) == 0 or res[-1] != a[i]:
            res.append(a[i])
        i += 1
    while j < m:
        if len(res) == 0 or res[-1] != b[j]:
            res.append(b[j])
        j += 1
    return res

a = [1, 2, 2, 3, 4, 5]
b = [2, 3, 3, 4, 5, 6]

print(findUnion(a,b))

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)