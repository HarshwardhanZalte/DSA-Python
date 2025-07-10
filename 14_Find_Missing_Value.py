def missingNumber(nums):
    n = len(nums)
    freq = {}
    for i in range(0,n+1):
        freq[i] = 0
    for i in nums:
        freq[i] = 1
    for k, v in freq.items():
        if v == 0:
            return k

a = [9,6,4,2,3,5,7,0,1]
print(missingNumber(a))

# Time Complexity: O(n)
# Space Complexity: O(n)