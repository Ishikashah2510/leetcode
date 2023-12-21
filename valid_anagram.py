class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            return True
        return False


sol_obj = Solution()
result = sol_obj.isAnagram(s="anagram", t="nagaram")
print(result)
