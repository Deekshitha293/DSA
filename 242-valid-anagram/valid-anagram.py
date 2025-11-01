class Solution:
    def isAnagram(self, s, t):
        # If lengths are different, not anagrams
        if len(s) != len(t):
            return False
        
        # Compare sorted versions of both strings
        return sorted(s) == sorted(t)
