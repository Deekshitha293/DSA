class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = set()

        # extract digits from the string
        for ch in s:
            if ch.isdigit():
                digits.add(int(ch))

        # if less than 2 unique digits, return -1
        if len(digits) < 2:
            return -1

        # remove the largest digit
        digits.remove(max(digits))

        # now the largest remaining is the second largest
        return max(digits)
