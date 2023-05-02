from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        print(len(nums))
        if k == 1:
            return nums
        if len(nums) <= k:
            return [max(nums)]

        all_windows = [0] * (len(nums)-k+1)
        print(len(all_windows))
        for i in range(int((len(nums)-k+1) / 2)):
            all_windows[i] = max(nums[i:i+k])
            all_windows[len(all_windows) - i - 1] = max(nums[len(nums)-k - i: len(nums) - i])
        return all_windows


sol_object = Solution()
answer = sol_object.maxSlidingWindow([], 0)
print(answer)
