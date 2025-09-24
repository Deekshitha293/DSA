class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')  # start with a very high number
        max_profit = 0             # no profit initially
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit
