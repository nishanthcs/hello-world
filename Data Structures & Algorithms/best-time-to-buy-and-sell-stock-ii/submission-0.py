class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_sum: int = 0

        for i in range(len(prices)-1):
            # you make transactions everyday comparing it with next day. 
            if(prices[i] < prices[i+1]):
                profit_sum += prices[i+1] - prices[i]
            
        return profit_sum