class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        counter = set()
        for r in range(len(s)):
            while s[r] in counter:
                counter.remove(s[l])
                l += 1
            counter.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
        