'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''
import copy
class Solution(object):
    def __init__(self, matrix):
        self._matrix = matrix
        
    def rotate(self):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix = copy.deepcopy(self._matrix)
        copy_matrix = copy.deepcopy(self._matrix)
        n = len(matrix)
        self.print_matrix(matrix)
        for i in range(n):#0,1,2
            for j in range(n):#0,1,2
                matrix[i][j] = copy_matrix[j][i]
                matrix[j][i] = copy_matrix[i][j]

        self.print_matrix(matrix)
        for row in matrix:
            row.reverse()

        self.print_matrix(matrix)
        return
                


    def print_matrix(self, matrix):
        '''
        print the matrxi
        '''
        for line in matrix:
            print ' '.join(str(e) for e in line)



s = Solution([[1,2,3], [4,5,6], [7,8,9]])
s.rotate()
