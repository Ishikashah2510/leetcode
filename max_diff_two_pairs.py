from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])


sol_obj = Solution()
result = sol_obj.maxProductDifference([5, 6, 7, 2, 4])
print(result)
