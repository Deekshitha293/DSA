class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # in case k > n
        temp = [0] * n
        
        for i in range(n):
            temp[(i + k) % n] = nums[i]  # new position
            
        for i in range(n):
            nums[i] = temp[i]  # copy back
