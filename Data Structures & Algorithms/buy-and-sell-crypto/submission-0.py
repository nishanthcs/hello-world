import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_idx, sell_idx = 0,1
        max_profit: int = 0

        while sell_idx < len(prices):
            buying_price = prices[buy_idx]
            selling_price = prices[sell_idx]

            if buying_price < selling_price:
                profit = selling_price - buying_price
                max_profit = max(max_profit, profit)
            else:
                # buy at selling price
                buy_idx = sell_idx
            
            sell_idx +=  1
        
        return max_profit