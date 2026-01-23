class Solution(object):
    def runningSum(self, nums):
        running_sum = []
        current_sum = 0
        
        for num in nums:
            current_sum += num
            running_sum.append(current_sum)
        
        return running_sum