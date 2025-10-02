class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            if window_sum > max_sum:
                max_sum = window_sum

        # Make sure to return float
        return max_sum / float(k)
