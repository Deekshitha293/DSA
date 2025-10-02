class Solution:
    def moveZeroes(self, nums):
        # Pointer for the position of the next non-zero element
        non_zero_index = 0

        # Step 1: Move all non-zero numbers to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1

        # Step 2: Fill the rest of the array with zeros
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0
