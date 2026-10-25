class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        
        res = []
        for l, r in queries:
            rmv = 0 if l == 0 else arr[l - 1]
            res.append(
                arr[r] ^ rmv
            )
        return res