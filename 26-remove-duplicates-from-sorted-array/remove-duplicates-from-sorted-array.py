class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 0  

        for j in range(1, len(nums)):  
            if nums[j] != nums[i]:     
                i += 1
                nums[i] = nums[j]      # place the unique number in correct position

        return i + 1  # total unique numbers
