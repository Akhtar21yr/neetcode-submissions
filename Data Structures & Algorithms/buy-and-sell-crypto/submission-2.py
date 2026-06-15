class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestbuy = prices[0]
        maxprofit = 0

        for i in prices:
            profit = i - bestbuy
            maxprofit = max(maxprofit,profit)
            bestbuy = min(bestbuy,i)



        return maxprofit
        