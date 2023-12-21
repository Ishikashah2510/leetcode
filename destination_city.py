from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        origins = []

        for each_pair in paths:
            origins.append(each_pair[0])

        for each_pair in paths:
            if each_pair[1] not in origins:
                return each_pair[1]


sol_obj = Solution()
result = sol_obj.destCity(paths=[["London", "New York"],
                                 ["New York", "Lima"],
                                 ["Lima", "Sao Paulo"]])
print(result)
