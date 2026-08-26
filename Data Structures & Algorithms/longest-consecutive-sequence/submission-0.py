class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        seq_len = 0
        for num in nums:
            if num - 1 not in seq:
                possible_seq = 1
                while num + 1 in seq:
                    possible_seq += 1
                    num += 1
                seq_len = max(seq_len, possible_seq)

        return seq_len
            

            


        