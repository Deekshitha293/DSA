class Solution(object):
    def reverse(self, x):
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check overflow (before adding digit
            if rev > (2**31 - 1) // 10:
                return 0

            rev = rev * 10 + digit

        return rev * sign

        