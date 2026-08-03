class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in prev_map:
                return [min(prev_map[n], i), max(prev_map[n], i)]
            else:
                prev_map[nums[i]] = i


        