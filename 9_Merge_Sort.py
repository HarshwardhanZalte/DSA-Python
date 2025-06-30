# def mergeSort(arr, l, r):
#     if l < r:
#         mid = (l + r)//2
#         mergeSort(arr,l,mid)
#         mergeSort(arr,mid+1,r)
#         return merge_array(arr,l,mid,r)
        
# def merge_array(arr,l,mid,r):
    
#     i = j = 0
#     k = l
#     left = arr[l:mid+1]
#     right = arr[mid+1:r+1]
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             arr[k] = left[i]
#             i+=1
#         else:
#             arr[k] = right[j]
#             j+=1
#         k+=1
#     while i < len(left):
#         arr[k] = left[i]
#         i+=1
#         k+=1
#     while j < len(right):
#         arr[k] = right[j]
#         j+=1
#         k+=1
#     return arr


def merge_array(left, right):
    res = []
    i, j = 0, 0
    n, m = len(left), len(right)
    while i < n and j < m:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    # res += left[i:] + right[j:]
    if i < n:
        while i < n:
            res.append(left[i])
            i += 1
    if j < m:
        while j < m:
            res.append(right[j])
            j += 1
    return res

def merge_Sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_Sort(arr[:mid])
    right = merge_Sort(arr[mid:])
    return merge_array(left, right)

arr = [64, 34, 25, 12, 22, 11, 90]
print(merge_Sort(arr))

# Time Complexity: O(n log n)
# Space Complexity: O(n)