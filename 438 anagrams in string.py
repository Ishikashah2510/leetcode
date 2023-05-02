from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indexes = []
        for each_ind in range(len(s) - len(p) + 1):
            if set(s[each_ind:len(p)+each_ind]) == set(p):
                if Counter(s[each_ind:len(p)+each_ind]) == Counter(p):
                    indexes.append(each_ind)
        return indexes


sol = Solution()
print(sol.findAnagrams("ababababab", "aab"))
