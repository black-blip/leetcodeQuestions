def maxProfit(prices):
    profit = 0

    low_cost = prices[0]

    for p in prices:
        low_cost = min(p,low_cost)

        profit = max(profit,abs(p-low_cost))

    return profit


prices = [7,1,5,3,6,4]
#maxprofit = 5

print(maxProfit(prices))