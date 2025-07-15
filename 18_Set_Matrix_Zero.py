def setMatrixZero(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row = set()
    col = set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
    for i in range(m):
        for j in range(n):
            if i in row or j in col:
                matrix[i][j] = 0        
    return matrix

matrix = [[1,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,1]]
print(setMatrixZero(matrix))