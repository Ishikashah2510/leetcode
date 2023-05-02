from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums = list(filter(lambda x: x > 0, nums))

        if not nums:
            return 1
        elif len(nums) == max(nums):
            return max(nums) + 1




sol_object = Solution()
answer = sol_object.firstMissingPositive([-1,-2])
print(answer)
