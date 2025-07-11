def twoSum(nums, target):
    n = len(nums)
    freq = {}
    for i in range(n):
        rem = target - nums[i]
        if rem in freq:
            return [freq[rem], i]
        freq[nums[i]] = i
    return []

a = twoSum([2, 7, 11, 15], 9)
print(a)

# Time Complexity: O(n)
# Space Complexity: O(n)