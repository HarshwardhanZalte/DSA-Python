# def reverseSubArray(arr,l,r):
#     # code here
#     if l >= r:
#         return arr
#     arr[l], arr[r] = arr[r], arr[l]
#     reverseSubArray(arr, l+1, r-1)

# n = [1, 2, 3, 4, 5]
# reverseSubArray(n,1, 4)
# print(n)

def reverseSubArray(arr,l,r):
    # code here
    fun(arr, l-1, r-1)
    return arr
    
def fun(arr, l, r):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    fun(arr, l+1, r-1)

n = [1, 2, 3, 4, 5]
reverseSubArray(n, 1, 4)
print(n)

# Time Complexity: O(n)
# Space Complexity: O(n)