class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # Initialize variables to keep track of minimum price and maximum profit
        min_price = prices[0]
        max_profit = 0

        # Iterate through the prices array
        for price in prices:
            # Update the minimum price if a lower price is encountered
            min_price = min(min_price, price)

            # Calculate the profit if we sell at the current price
            profit = price - min_price

            # Update the maximum profit if a higher profit is encountered
            max_profit = max(max_profit, profit)

        return max_profit




