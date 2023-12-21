from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for num in nums1:
            checking = False
            found = False
            for sec_num in nums2:
                if num == sec_num:
                    checking = True

                if checking and sec_num > num:
                    result.append(sec_num)
                    found = True
                    break

            if not found:
                result.append(-1)

        return result


sol_obj = Solution()
result = sol_obj.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
print(result)
