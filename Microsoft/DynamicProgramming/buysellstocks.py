class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dynamic programming solution
        n = len(prices)
        if n < 2:
            return 0
        max_profit, min_stock = float('-inf'), prices[0]
        
        for price in prices:
            max_profit = max(max_profit, price - min_stock)
            min_stock = min(min_stock, price)
            
                
        return max_profit
        