from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # best_area = 0
        #
        # for left_x, x_height in enumerate(height):
        #     for left_y, y_height in enumerate(height[left_x+1:]):
        #         # actual_y = left_y+left_x+1
        #         current_area = min(x_height, y_height) * (left_y + 1)
        #         if current_area > best_area:
        #             best_area = current_area

        best_area = 0
        right = len(height) - 1
        left = 0

        while True:
            if right == left:
                break

            current_area = min(height[left], height[right]) * (right - left)
            if current_area > best_area:
                best_area = current_area

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return best_area


sol_object = Solution()
answer = sol_object.maxArea([1,8,6,2,5,4,8,3,7])
print(answer)