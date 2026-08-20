class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            encoded_string += string
            encoded_string += '\n'
        return encoded_string

    def decode(self, s: str) -> List[str]:
        possible_strs = []
        for letter in s:
            if letter == '\n':
                possible_strs.append('')
        i = 0
        for letter in s:
            if letter != '\n':
                possible_strs[i] += letter
            if letter == "\n":
                i += 1
                continue
        return possible_strs
            





