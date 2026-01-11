class Solution(object):
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])
        
        # if reshape not possible
        if m * n != r * c:
            return mat
        
        # flatten original matrix
        flat_list = []
        for row in mat:
            for val in row:
                flat_list.append(val)
        
        # fill new matrix
        new_mat = [[0] * c for _ in range(r)]
        index = 0
        for i in range(r):
            for j in range(c):
                new_mat[i][j] = flat_list[index]
                index += 1
                
        return new_mat
