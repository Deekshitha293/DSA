class Solution:
    def plusOne(self, digits):
        # Step 1: Traverse from rightmost digit to left
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1  # add 1
            if digits[i] < 10:  # no carry
                return digits
            digits[i] = 0  # digit becomes 10 → set to 0 and carry goes left
        
        # Step 2: If all digits were 9, add 1 at the front
        return [1] + digits
