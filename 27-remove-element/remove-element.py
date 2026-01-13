class Solution:
    def removeElement(self, nums, val):
        k = 0  # next position for valid element
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k

# Example usage
nums = [0,1,2,2,3,0,4,2]
val = 2
sol = Solution()
k = sol.removeElement(nums, val)

print("k =", k)
print("Modified nums =", nums[:k])
