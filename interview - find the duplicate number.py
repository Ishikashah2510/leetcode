from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_count = {}
        for num in nums:
            if num in num_count.keys():
                num_count[num] += 1
                if num_count[num] > 1:
                    return num
            else:
                num_count[num] = 1


sol_object = Solution()
answer = sol_object.findDuplicate([1,1,2,3,4])
print(answer)
