def rearrangeArray(nums):
    pos = 0
    neg = 1
    n = len(nums)
    res = [0] * n
    for i in range(0,n):
        if nums[i] >= 0:
            res[pos] = nums[i]
            pos += 2
        else:
            res[neg] = nums[i]
            neg +=2
    return res

# Time Complexity: O(n)
# Space Complexity: O(n)




def rearrangeArray2(nums):
    pos = []
    neg = []
    n = len(nums)
    for i in range(0,n):
        if nums[i] >= 0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])
    for i in range(0, n//2):
        nums[2*i] = pos[i]
        nums[(2*i)+1] = neg[i]
    return nums

# Time Complexity: O(n)
# Space Complexity: O(1)

nums = [-1, 2, -3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print(rearrangeArray(nums))