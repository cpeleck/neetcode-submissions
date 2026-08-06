class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k
        

    def add(self, val: int) -> int:
        prev_len = len(self.nums)
        for i, num in enumerate(self.nums):
            if val <= num:
                self.nums.insert(i ,val)
                break
        if prev_len == len(self.nums):
            self.nums.append(val)
        return self.nums[-self.k]

        
