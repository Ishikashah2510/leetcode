from typing import List
import copy
import numpy


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        old_matrix = copy.deepcopy(matrix)
        for ind, each_row in enumerate(old_matrix):
            if each_row.count(0):
                matrix[ind] = [0] * len(each_row)
            print(each_row)

        zero_index = []
        for each_row in old_matrix:
            temp_arr = numpy.array(each_row)
            zero_indices = list(numpy.where(temp_arr == 0)[0])
            if len(zero_indices) > 0:
                zero_index.extend(zero_indices)

        zero_index = set(zero_index)

        for ind, each_row in enumerate(matrix):
            for each_ind in zero_index:
                matrix[ind][each_ind] = 0

        print(zero_index)
        print(matrix)


sol_object = Solution()
sol_object.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
