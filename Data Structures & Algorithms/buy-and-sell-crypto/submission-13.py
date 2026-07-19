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
                maxSellIndex = i
            print(minBuy, maxSell,  maxSell - minBuy, maxSellIndex > minBuyIndex)
            if maxSell - minBuy > maxProfit and maxSellIndex > minBuyIndex:
                maxProfit = maxSell - minBuy
        print(maxSell, minBuy)
        # maxProfit = maxSell - minBuy
        # if maxSell - minBuy > maxProfit and maxSellIndex > minBuyIndex:
        #         maxProfit = maxSell - minBuy
        if maxProfit < 0:
            return 0
        return maxProfit

            