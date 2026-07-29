class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1 or len(s) % 2 == 1:
            return False
        l = 0
        r = len(s) - 1
        for i in range(len(s)):
            if l >= len(s) - 1:
                return True
            if s[l] == '(':
                if ord(s[l]) + 1 == ord(s[r]) or ord(s[l]) + 1 == ord(s[l+1]):
                    if ord(s[l]) + 1 == ord(s[r]):
                        r -= 1
                    if ord(s[l]) + 1 == ord(s[l+1]):
                        l += 1
                else:
                    return True if l > r else False
            else:
                if ord(s[l]) + 2 == ord(s[r]) or ord(s[l]) + 2 == ord(s[l+1]):
                    if ord(s[l]) + 2 == ord(s[r]):
                        r -= 1
                    if ord(s[l]) + 2 == ord(s[l+1]):
                        l += 1
                else:
                    return True if l > r else False
            l += 1
            