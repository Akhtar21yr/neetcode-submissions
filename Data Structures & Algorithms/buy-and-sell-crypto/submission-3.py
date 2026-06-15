class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for x in prices:
            if x< min_price:
                min_price = x

            else:
                profit = x-min_price
                max_profit = max(max_profit, profit)

        return max_profit