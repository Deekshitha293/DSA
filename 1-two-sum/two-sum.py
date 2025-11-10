class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store number -> index m
        num_dict = {}

        # Iterate over the array
        for i, num in enumerate(nums):
            complement = target - num  # what we need to find
            if complement in num_dict:
                # Found the pair, return their indices
                return [num_dict[complement], i]
            # Stores current number and its index
            num_dict[num] = i

        # In case no solution is found 
        return []
