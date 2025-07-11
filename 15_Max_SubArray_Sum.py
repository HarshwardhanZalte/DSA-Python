# def maxSubArray(nums):
#         n = len(nums)
#         max = float('-inf')
#         for i in range(n):
#             total = 0
#             for j in range(i, n):
#                 total += nums[j]
#                 if total > max:
#                     max = total
#         return max


def maxSubArray(nums):
    n = len(nums)
    max = float('-inf')
    total = 0
    for i in range(n):
        if total < 0:
            total = 0
        total += nums[i]
        if total > max:
            max = total
    return max

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)