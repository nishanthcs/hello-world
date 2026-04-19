class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buying decision
        # profit after buying ith, profile after dont buy ith 
        # selling decision
        # profit after selling ith, profit after do not selling ith 

        can_buy = True
        i = 0; 
        bought_idx = -1 # means you can buy
        # Store (idx, can_buy) with the profit at that index
        dp = {}

        def dfs(idx, can_buy):
            if idx >= len(prices):
                return 0
            if (idx, can_buy) in dp:
                return dp.get((idx,can_buy))

            
            # Using DFS and maintaining a ledger ; if you BUY you subtract and if you SELL, you add to the profits
            if can_buy:
                # if can buy is true, you can buy now 
                # you bought at prices[i] which means you record i 
                # then you add the profit from selling it later
                # You are 
                b_profit =  dfs(idx+1, not can_buy) - prices[idx] 
                
                # You are not choosing buy here
                nb_profit = dfs(idx+1, can_buy)

                profit = max(b_profit, nb_profit)
            else:
                # selling now but add the profit from buy/sell later after cooldown
                s_profit = dfs(idx+2, True) + prices[idx]

                # sell later
                ns_profit = dfs(idx+1, can_buy)

                profit = max(s_profit, ns_profit)

            dp[(idx,can_buy)] = profit
            return profit

        
        return dfs(i, bought_idx)


                


