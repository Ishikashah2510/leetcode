from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        not_poss_rows = []
        not_poss_cols = []

        total_special = 0

        m = len(mat)
        n = len(mat[0])


sol_obj = Solution()
result = sol_obj.numSpecial(mat=[[1, 0, 1],
                                 [0, 0, 1],
                                 [0, 1, 0]])
print(result)
