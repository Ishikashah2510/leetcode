class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", '')
        return int(eval(s))


sol_object = Solution()
answer = sol_object.calculate('14/3*2')
print(answer)
