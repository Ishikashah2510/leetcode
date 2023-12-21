from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        possibilities = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) < target:
                    possibilities += 1

        return possibilities


sol_obj = Solution()
result = sol_obj.countPairs(nums = [-1,1,2,3,1], target = 2)
print(result)
