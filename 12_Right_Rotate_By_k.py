def rightRotate1(arr, k):
     for i in range(0, k):
        e =  arr.pop()
        arr.insert(0, e)

# Time Complexity: O(k)
# Space Complexity: O(1)

def rightRotate2(arr, k):
    n = len(arr)
    arr[:] = arr[n-k:] + arr[:n-k]

# Time Complexity: O(n)
# Space Complexity: O(1)

def rightRotate3(arr, k):
    n = len(arr)
    for i in range(0, k):
        e = arr[n-1]
        for j in range(n-1, 0, -1):
            arr[j] = arr[j-1]
        arr[0] = e

# Time Complexity: O(n)
# Space Complexity: O(1)

def rightRotate(nums, k):
    k %= len(nums)
    def rev(st,end):
        while st<end:
            nums[st],nums[end] = nums[end],nums[st]
            st+=1
            end-=1
    rev(0,len(nums)-1)
    rev(0,k-1)
    rev(k,len(nums)-1)

# Time Complexity: O(n)
# Space Complexity: O(1)

arr = [1, 2, 3, 4, 5]
rightRotate1(arr, 2)
print(arr)

arr = [1, 2, 3, 4, 5]
rightRotate2(arr, 2)
print(arr)

arr = [1, 2, 3, 4, 5]
rightRotate3(arr, 2)
print(arr)

arr = [1, 2, 3, 4, 5]
rightRotate(arr, 2)
print(arr)