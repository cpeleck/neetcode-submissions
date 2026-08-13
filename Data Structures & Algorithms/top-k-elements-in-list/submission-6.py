class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        buckets = [[] for i in range(len(nums) + 1)]
    
        for num in nums:
            cnt[num] = 1 + cnt.get(num, 0)
            # counts how many times a number is occured at that number
            # ie for nums[1,1,2,2,2] 1 -> 3
        for num, count in cnt.items():
            buckets[count].append(num)
            # we put this number at the corresponding bucket
            # so bucket 3 will get 1
        
        result = []
        for i in range(len(buckets) - 1, 0, -1): # read backwards so we get most frequent first
            for num in buckets[i]:
                # add this number to the result
                result.append(num)
                if len(result) == k:
                    return result
        