class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 0
        nxt = 1
        maxProfit = 0
        
        while nxt < len(prices):
            profit = prices[nxt] - prices[curr]
            if prices[nxt] > prices[curr]:
                maxProfit = max(profit, maxProfit)
            else:
                curr = nxt
            nxt += 1
        return maxProfit