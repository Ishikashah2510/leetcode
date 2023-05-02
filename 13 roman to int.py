class Solution:
    def romanToInt(self, s: str) -> int:
        minuses = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        sum = 0
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        skip = -1
        for ind, curr_letter in enumerate(s):
            if ind == skip:
                continue
            if s[ind:ind+2] in minuses.keys():
                sum += minuses[s[ind:ind+2]]
                skip = ind + 1
            else:
                sum += values[curr_letter]
        return sum


sol = Solution()
print(sol.romanToInt('LVIII'))
