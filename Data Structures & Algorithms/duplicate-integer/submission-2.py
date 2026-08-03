class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        
        d = set()
        for num in nums:
            if num in d:
                return True
            else:
                d.add(num)
        return False

