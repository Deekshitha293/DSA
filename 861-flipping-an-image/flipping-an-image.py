class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(image)):
            image[i]=image[i][::-1]
            for j in range(len(image[i])):
                image[i][j] = 1 - image[i][j]

        return image