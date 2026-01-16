class Solution(object):
    def findDuplicate(self, nums):  # add 'self' as first parameter
        # Phase 1: Find intersection point
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: Find entrance to cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

# Create an object of the class
sol = Solution()

# Test examples
print(sol.findDuplicate([1,3,4,2,2]))  # Output: 2
print(sol.findDuplicate([3,1,3,4,2]))  # Output: 3
print(sol.findDuplicate([3,3,3,3,3]))  # Output: 3
