from typing import List


class Solution:
    def find_new_point(self, pointa, pointb):
        min_x = pointa[0]

        if pointb[0] > min_x:
            min_x = min_x + 1
        elif pointb[0] < min_x:
            min_x = min_x - 1

        min_y = pointa[1]
        if pointb[1] > min_y:
            min_y = min_y + 1
        elif pointb[1] < min_y:
            min_y = min_y - 1

        return [min_x, min_y]

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        curr_point = points[0]
        time = 0
        pointer = 1

        while curr_point != points[-1]:
            curr_point = self.find_new_point(curr_point, points[pointer])
            time += 1

            if curr_point == points[pointer]:
                pointer += 1

        return time


sol_obj = Solution()
result = sol_obj.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
print(result)
