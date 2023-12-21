from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_len = 0

        for each_word in words:
            form_okay = True

            for each_letter in set(each_word):
                if each_word.count(each_letter) > chars.count(each_letter):
                    form_okay = False
                    break

            if form_okay:
                total_len += len(each_word)

        return total_len


sol_obj = Solution()
result = sol_obj.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr")
print(result)
