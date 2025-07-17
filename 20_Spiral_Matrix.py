def spiralOrder(matrix):
    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Top row
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1

        # Right column
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # Bottom row
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            # Left column
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

    return res


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(spiralOrder(matrix))

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)