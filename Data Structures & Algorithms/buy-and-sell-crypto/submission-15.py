class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0

        minBuy = 100
        minBuyIndex = 0

        maxSell = 0
        maxSellIndex = len(prices)-1

        for i, price in enumerate(prices):
            if price < minBuy:
                minBuy = price
                minBuyIndex = i
            elif price - minBuy > maxProfit and i > minBuyIndex:
                maxSell = price
                maxProfit = maxSell - minBuy
                maxSellIndex = i
        if maxProfit < 0:
            return 0
        return maxProfit

            