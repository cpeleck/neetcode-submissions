class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = {
            1: 1,
            2: 2,
            3: 3,
        }
        if n <= 3:
            return n
        for i in range(4, n+1):
            stairs[i] = stairs[i-1] + stairs[i- 2]
        return stairs[n]
        