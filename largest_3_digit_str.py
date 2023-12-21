class Solution:
    def largestGoodInteger(self, num: str) -> str:
        curr_max = -10000000000000

        for i in range(len(num)-2):
            temp_num = num[i: i+3]
            if len(set(temp_num)) == 1:
                if int(temp_num) > int(curr_max):
                    curr_max = temp_num

        curr_max = "" if curr_max == -10000000000000 else curr_max
        return curr_max


sol_obj = Solution()
result = sol_obj.largestGoodInteger("6777133339")
print(result)
