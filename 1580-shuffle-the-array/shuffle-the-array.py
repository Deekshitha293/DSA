class Solution(object):
    def shuffle(self, nums, n):
        x = nums[:n]   
        y = nums[n:]   # second half
        result = []

        for i in range(n):
            result.append(x[i])
            result.append(y[i])

        return result
