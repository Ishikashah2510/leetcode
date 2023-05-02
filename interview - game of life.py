from typing import List
import copy


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        old_board = copy.deepcopy(board)

        for x in range(len(old_board)):
            for y in range(len(old_board[x])):

                is_live = 0
                for subx in range(x - 1, x + 2):
                    for suby in range(y - 1, y + 2):
                        if (0 <= subx < len(old_board)) and (0 <= suby < len(old_board[x])):
                            if subx == x and suby == y:
                                continue
                            if old_board[subx][suby] == 1:
                                is_live += 1
                # cell is dead
                if old_board[x][y] == 0 and is_live == 3:
                    board[x][y] = 1

                # cell is live
                elif is_live not in [2, 3]:
                        board[x][y] = 0

        print(old_board)
        print(board)


sol_object = Solution()
sol_object.gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
