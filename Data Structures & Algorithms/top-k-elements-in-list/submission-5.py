class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        buckets = [[] for i in range(len(nums) + 1)]
    
        for num in nums:
            cnt[num] = 1 + cnt.get(num, 0)
        for num, count in cnt.items():
            buckets[count].append(num)
        
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        