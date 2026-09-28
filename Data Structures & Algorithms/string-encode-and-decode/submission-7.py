class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            encoded_str += s
            encoded_str += '\n'
        return encoded_str

    def decode(self, s: str) -> List[str]:
        soln = []
        curr_word = ''
        for i in range(len(s)):
            if s[i] == '\n':
                soln.append(curr_word)
                curr_word = ''
            else:
                curr_word += s[i]
        return soln

