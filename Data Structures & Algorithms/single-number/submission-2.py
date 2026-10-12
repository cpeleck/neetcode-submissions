class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        for n, c in count.items():
            if c == 1:
                return n
        