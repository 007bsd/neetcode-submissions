class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        lowest_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            current_price = prices[i]
            profit_if_sell_today = current_price - lowest_price
            max_profit = max(max_profit, profit_if_sell_today)
            lowest_price = min(lowest_price, current_price)
        return max_profit
        

        