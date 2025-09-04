from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            min_price = min(price, min_price)
            max_profit = max(max_profit, (price-min_price))
        return max_profit
sol = Solution()
prices = [10,1,5,6,7,1]
prices = [10,8,7,5,2]
print(sol.maxProfit(prices))