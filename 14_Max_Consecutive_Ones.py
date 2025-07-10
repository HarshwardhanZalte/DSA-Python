def findMaxConsecutiveOnes(nums):
        c = 0
        mc = 0
        n = len(nums)
        for i in range(0, n):
            if nums[i] == 1:
                c += 1
            else:
                mc = max(mc, c)
                c = 0
        return max(mc,c)
    
    
a = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(a))
    # Time Complexity: O(n)
    # Space Complexity: O(1)