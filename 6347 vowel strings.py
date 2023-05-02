from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        response = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        for each_query_range in queries:
            ans = 0
            # print("each_query_range: ", each_query_range)
            for each_word in words[each_query_range[0]: each_query_range[1] + 1]:
                # print("each_word: ", each_word)
                if each_word[0].lower() in vowels and each_word[-1] in vowels:
                    ans += 1
            response.append(ans)
        return response


sol = Solution()
print(sol.vowelStrings(["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]]))
