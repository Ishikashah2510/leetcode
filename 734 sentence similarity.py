from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        for ind in range(len(sentence1)):
            if sentence1[ind] == sentence2[ind]:
                continue
            if [sentence1[ind], sentence2[ind]] not in similarPairs:
                if [sentence2[ind], sentence1[ind]] not in similarPairs:
                    return False
        return True


sol = Solution()
print(sol.areSentencesSimilar(["great","acting","skills"], ["fine","drama","talent"],
                              [["great","fine"],["drama","acting"],["skills","talent"]]))
