class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            freq[n] += 1
        
        for n, c in freq.items():
            buckets[c].append(n)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for b in buckets[i]:
                res.append(b)
                if len(res) == k:
                    return res
