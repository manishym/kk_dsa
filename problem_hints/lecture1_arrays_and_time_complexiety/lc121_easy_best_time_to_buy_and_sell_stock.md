
# 121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock


## Easy approach (Two variables)
1. Initialize variables:
   - min_price = infinity (or first price)
   - max_profit = 0
2. For each price in prices array:
   - Update min_price if current price is lower
   - Calculate potential profit: current_price - min_price
   - Update max_profit if potential profit is higher
3. Return max_profit

Time complexity: O(n) - we iterate through array once
Space complexity: O(1) - we only use two variables


## Brute force approach (not recommended)
1. For each price at index i:
   - Check all prices after index i
   - Calculate profit: price[j] - price[i]
   - Keep track of maximum profit seen
2. Return maximum profit

Time complexity: O(n²) - nested loops
Space complexity: O(1) - only need a few variables

