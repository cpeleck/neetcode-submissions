class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_close = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        for p in s:
            if p in open_to_close.keys():
                if stack and stack[-1] == open_to_close[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        if stack:
            return False
        else:
            return True
            