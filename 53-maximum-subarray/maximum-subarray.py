class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]       # store maximum sum so far
        current_sum = 0         # running sum
        
        for num in nums:
            if current_sum < 0:  # if current sum is negative, discard it
                current_sum = 0
            current_sum += num
            max_sum = max(max_sum, current_sum)  # update max_sum
        
        return max_sum
