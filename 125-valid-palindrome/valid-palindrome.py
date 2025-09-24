class Solution:
    def isPalindrome(self, s):
        # Normalize string: lowercase + keep only alphanumeric characters
        s = ''.join(char.lower() for char in s if char.isalnum())
        
        # Two-pointer check
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True
