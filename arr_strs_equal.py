from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if "".join(word1) == "".join(word2):
            return True
        return False


sol_obj = Solution()
result = sol_obj.arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"])
print(result)

