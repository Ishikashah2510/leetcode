from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        output_list = []

        if not nums:
            if lower == upper:
                output_list.append(f"{lower}")
            else:
                output_list.append(f"{lower}->{upper}")

        else:
            if lower != nums[0]:
                if lower + 1 == nums[0]:
                    output_list.append(f"{lower}")
                else:
                    output_list.append(f"{lower}->{nums[0]-1}")

            for ind, each_num in enumerate(nums[:-1]):
                if nums[ind+1] - each_num != 1:
                    if each_num + 1 == nums[ind+1] - 1:
                        output_list.append(f"{each_num+1}")
                    else:
                        output_list.append(f"{each_num+1}->{nums[ind+1]-1}")

            if nums[-1] != upper:
                if nums[-1] + 1 == upper:
                    output_list.append(f"{upper}")
                else:
                    output_list.append(f"{nums[-1]+1}->{upper}")

        return output_list


sol_object = Solution()
answer = sol_object.findMissingRanges([], -1, 100)
print(answer)
