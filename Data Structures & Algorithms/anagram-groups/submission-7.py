class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            res[tuple(freq)].append(s)
        
        return_list = []
        for value in res.values():
            return_list.append(value)
        return return_list


        