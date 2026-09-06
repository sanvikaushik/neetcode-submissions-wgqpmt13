class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        for i in range(len(prices) - 1):

            b = prices[i]
            l = i + 1

            while l < len(prices):
                if prices[l] > b:
                    max_profit = max(max_profit, prices[l] - b)
                l += 1

        if max_profit >= 0:
            return max_profit
        else: 
            return 0
