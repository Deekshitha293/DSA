class Solution:
    def plusOne(self, digits):
        
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1  # add 1
            if digits[i] < 10:  # no carry
                return digits
            digits[i] = 0  
        
        
        return [1] + digits
