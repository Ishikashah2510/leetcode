class Solution:
    def totalMoney(self, n: int) -> int:
        money = 0
        monday_money = 1
        prev_day_money = 0

        for i in range(n):
            if i % 7 == 0:
                money += (monday_money * 1)
                prev_day_money = monday_money
                monday_money += 1
            else:
                prev_day_money += 1
                money += prev_day_money

        return money


sol_obj = Solution()
result = sol_obj.totalMoney(10)
print(result)