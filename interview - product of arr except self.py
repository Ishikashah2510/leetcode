from typing import List
import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        left_prods = [0] * len(nums)
        right_prods = [0] * len(nums)

        left_prods[0] = 1
        for i in range(1, len(nums)):
            left_prods[i] = left_prods[i-1] * nums[i-1]

        right_prods[-1] = 1
        for i in reversed(range(len(nums)-1)):
            right_prods[i] = right_prods[i+1] * nums[i+1]

        for i in range(len(nums)):
            answer.append(left_prods[i] * right_prods[i])

        # for i in range(len(nums)):
            # 18/22 passed, but still time limit exceeded for bigger inputs
            # answer.append(1)
            # answer.append(math.prod(nums[0:i] + nums[i+1:]))

            # brute force approach
            # for j in range(len(nums)):
            #     if j == i:
            #         continue
            #     answer[i] *= nums[j]

        return answer


sol = Solution()
final_answer = sol.productExceptSelf([1, 2, 3, 4])
print(final_answer)

# nums = [2, 1, 3, 4]
# print(nums[0:1] + nums[2:])

# [1, 2, 3]
# i -> current index
# answer -> final list
# answer[all-i] * nums[i]
# answer[i] = nums[all-i]
