class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_freq = [0] * 26
        for c in p:
            p_freq[ord(c) - ord('a')] += 1

        l = 0
        res = []
        for r in range(len(p), len(s)+1):
            window = s[l:r]
            freq = [0] * 26
            for c in window:
                freq[ord(c) - ord('a')] += 1
            if freq == p_freq:
                res.append(l)
            l += 1
        return res

