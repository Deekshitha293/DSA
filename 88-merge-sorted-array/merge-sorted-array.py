class Solution:
    def merge(self, nums1, m, nums2, n):
        # Start from the e
        i = m - 1   # last valid element in nums1
        j = n - 1   # last element in nums2
        k = m + n - 1   # last position in nums1 (extra space)

        # Compare from the back and place bigger one at the end
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 still has elements, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
