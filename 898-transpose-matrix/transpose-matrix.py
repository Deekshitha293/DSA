class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        # This will hold the transposed matrix
        transpose = []
        
        # Loop over each column in the original matrix
        for i in range(cols):
            new_row = []  # new row for transpose
            for j in range(rows):
                new_row.append(matrix[j][i])  # take element from original
            transpose.append(new_row)  # add the row to transpose
        
        return transpose
