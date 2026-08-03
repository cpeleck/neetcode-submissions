class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find the biggest difference in price but j > i
        biggest_diff = 0
        for i in range(len(prices)):
            for j in range(1, len(prices)):
                if i >= j:
                    continue
                diff = prices[j] - prices[i]
                if diff > biggest_diff:
                    biggest_diff = diff


        return biggest_diff

        