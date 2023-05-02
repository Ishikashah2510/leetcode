from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = 1000000000
        min2 = 1000000000

        for num in nums:
            if num < min1:
                min1 = num

            if num > min1:
                min2 = min([num, min2])

            if num > min2:
                return True

        return False


sol_object = Solution()
answer = sol_object.increasingTriplet([4,5,2147483647,1,2])
print(answer)
