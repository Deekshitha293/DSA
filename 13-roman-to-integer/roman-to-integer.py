class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Map Roman symbols to values
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Process each character from right to left
        for ch in reversed(s):
            value = roman[ch]
            # If current value is less than previous, subtract it
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        return total