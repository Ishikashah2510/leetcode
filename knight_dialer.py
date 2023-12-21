class Solution:
    def knightDialer(self, n: int) -> int:

        if n == 1 or n == 2:
            return 10 * n

        possible_no_moves = [2, 2, 2, 2, 3, 0, 3, 2, 2, 2]
        possible_moves = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4]
        ]

        total_moves = 0

        mid_count = [1] * 10
        for i in range(2, n):
            temp_count = [0] * 10
            for each_step in range(10):
                for next_step in possible_moves[each_step]:
                    temp_count[next_step] += mid_count[each_step]

            mid_count = temp_count

        for i in range(10):
            total_moves += (possible_no_moves[i] * mid_count[i])

        return total_moves % (10**9 + 7)


sol_obj = Solution()
result = sol_obj.knightDialer(3131)
print(result)
