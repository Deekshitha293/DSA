class Solution(object):
    def thirdMax(self, nums):
        # Remove duplicates
        nums = list(set(nums))

        # Sort in descending order
        nums.sort(reverse=True)

        # If we have at least 3 distinct numbers
        if len(nums) >= 3:
            return nums[2]  # third maximum
        else:
            return nums[0]  # maximum
