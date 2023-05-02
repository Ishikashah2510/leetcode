from typing import List
import math


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for moment in range(k):
            gifts[gifts.index(max(gifts))] = int(math.sqrt(max(gifts)))

        return sum(gifts)


sol = Solution()
print(sol.pickGifts([1, 1, 1, 1], 4))
