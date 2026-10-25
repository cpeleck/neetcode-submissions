class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charset = set()
        longest = 0
        for r, c in enumerate(s):
            while c in charset:
                charset.remove(s[l])
                l += 1
            charset.add(c)
            longest = max(longest, r - l + 1)
        return longest


        