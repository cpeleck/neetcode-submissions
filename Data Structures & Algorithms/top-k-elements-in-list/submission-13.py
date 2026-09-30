class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amt = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            amt[n] += 1
        
        for n, c in amt.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
