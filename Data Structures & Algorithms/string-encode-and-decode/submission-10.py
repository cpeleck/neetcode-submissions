class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = []
        for s in strs:
            encode.append(str(len(s)))
            encode.append('#')
            encode.append(s)
        return ''.join(encode)

    def decode(self, s: str) -> List[str]:
        # 2#we3#say1#:3#yes10#!@#$%^&*()
        # 5#Hello5#World
        decode = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decode.append(s[i:j])
            i = j
        return decode


        
