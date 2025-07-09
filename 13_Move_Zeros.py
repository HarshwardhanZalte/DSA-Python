def moveZeroes(nums):
    n = len(nums)
    temp = []
    for i in range(0,n):
        if nums[i] != 0:
            temp.append(nums[i])
    nz = len(temp)
    for i in range(0, nz):
        nums[i] = temp[i]
    for i in range(nz, n):
        nums[i] = 0
    return nums

arr = [0, 1, 0, 3, 12]
print(moveZeroes(arr))

# Time Complexity: O(n)
# Space Complexity: O(n)

