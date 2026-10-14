class Solution:
    def reverseBits(self, n: int) -> int:
        res = [0] * 32
        for i in range(32):
            res[i] = (n & 1)
            n >>= 1
        num = 0
        for i, m in enumerate(range(32, 0, -1)):
            num += (res[i] * (2 ** m))   
        return num//2
        