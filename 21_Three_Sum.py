def ThreeSum(arr):
    arr.sort()
    res = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        l, r = i+1, len(arr)-1
        while l < r:
            sum = arr[i] + arr[l] + arr[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                res.append([arr[i], arr[l], arr[r]])
                while l < r and arr[l] == arr[l+1]:
                    l += 1
                while l < r and arr[r] == arr[r-1]:
                    r -= 1
                l += 1
                r -= 1
    return res

arr = [-1, 0, 1, 2, -1, -4]
print(ThreeSum(arr))

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = set()
        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ele = [nums[i], nums[j], nums[k]]
                        ele.sort()
                        res.add(tuple(ele))
        return list(res)
    
    # Time Complexity: O(n^3)
    # Space Complexity: O(n^2)