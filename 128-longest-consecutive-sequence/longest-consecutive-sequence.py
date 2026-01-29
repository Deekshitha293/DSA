class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        num_set = set(nums)
        longest = 0

        for num in num_set:
            # check if this is the start of a sequence
            if num - 1 not in num_set:
                current = num
                count = 1

                # count the length of the sequence
                while current + 1 in num_set:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest
