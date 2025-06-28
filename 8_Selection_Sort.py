def selectionSort(arr):
    #code here
    n = len(arr)
    for i in range(0, n):
        min_ind = i
        for j in range(i+1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(selectionSort(arr))