from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        distinct_elements = set(arr)
        ele_25 = len(arr) / 4

        for each_element in distinct_elements:
            if arr.count(each_element) > ele_25:
                return each_element


sol_obj = Solution()
result = sol_obj.findSpecialInteger([1,2,2,6,6,6,6,7,10])
print(result)
