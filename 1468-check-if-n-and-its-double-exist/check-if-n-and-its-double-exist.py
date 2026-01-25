class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()

        for num in arr:
            # check if double or half already exists
            if (2 * num) in seen or (num % 2 == 0 and (num // 2) in seen):
                return True

            # add current number to set
            seen.add(num)

        return False