class Solution:
    def numberOfMatches(self, n: int) -> int:
        no_of_matches = 0

        while n != 1:
            if n % 2 == 0:
                no_of_matches += int(n/2)
                n = int(n/2)
            else:
                no_of_matches += int((n-1)/2)
                n = int((n-1)/2) + 1

        return no_of_matches


sol_obj = Solution()
result = sol_obj.numberOfMatches(14)
print(result)
