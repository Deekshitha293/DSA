class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        total = 0
        
        for i in range(n):
            # Add primary diagonal element
            total += mat[i][i]
            
            # Add secondary diagonal element
            total += mat[i][n-1-i]
        
        # If n is odd, subtract the middle element once (it was counted twice)
        if n % 2 == 1:
            total -= mat[n//2][n//2]
        
        return total
