def linearSearch(nums, target):
    for i in range(0, len(nums)):
        if nums[i] == target:
            return i
    return -1

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = linearSearch(nums, target)
print(result)

# Time Complexity: O(n)
# Space Complexity: O(1)