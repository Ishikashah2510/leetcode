from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        :param nums: list of input numbers
        :return: string of largest number string
        """
        str_nums = list(map(lambda each_num: str(each_num), nums))
        str_nums.sort(reverse=True, key=lambda e: (e, -len(e), e[0]))
        print(str_nums)
        return "".join(str_nums)


sol_object = Solution()
answer = sol_object.largestNumber([3,30,34,5,9])
print(answer)
