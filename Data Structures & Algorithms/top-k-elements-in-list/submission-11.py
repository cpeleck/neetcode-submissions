class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        buck = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1

        for n, c in count.items():
            buck[c].append(n)

        soln = []
        for i in range(len(buck) - 1, 0, -1):
            for n in buck[i]:
                soln.append(n)
                if len(soln) == k:
                    return soln
