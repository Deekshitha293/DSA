class Solution(object):
    def replaceElements(self, arr):
        n = len(arr)
        max_so_far = -1  # the last element should be replaced with -1

        # traverse from right to left
        for i in range(n-1, -1, -1):
            current = arr[i]        # store current value
            arr[i] = max_so_far      # replace current with max seen so far
            if current > max_so_far:
                max_so_far = current  # update max_so_far if current is greater

        return arr
