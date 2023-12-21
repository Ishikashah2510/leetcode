from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        ones_rows = [0] * m
        ones_cols = [0] * n

        for i in range(m):
            for j in range(n):
                ones_rows[i] += grid[i][j]
                ones_cols[j] += grid[i][j]

        diff = []

        for i in range(m):
            sub_list = []
            for j in range(n):
                sub_list.append(2 * (ones_rows[i] + ones_cols[j]) - n - m)

            diff.append(sub_list)

        return diff


sol_obj = Solution()
result = sol_obj.onesMinusZeros([[0, 1, 1],
                                 [1, 0, 1],
                                 [0, 0, 1]])
print(result)
