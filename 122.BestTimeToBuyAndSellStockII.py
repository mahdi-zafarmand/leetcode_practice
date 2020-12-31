class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        
        while i < len(prices) - 1:
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
            i += 1
        return profit
        
        
#         start = 0
#         while i < len(prices) - 1:
#             j = i
#             start = i
#             while j < len(prices) - 1 and prices[j] >= prices[j + 1]:
#                 i += 1
#                 j += 1
#             start = j
#             while j < len(prices) - 1 and prices[j] <= prices[j + 1]:
#                 i += 1
#                 j += 1
#             profit += prices[j] - prices[start]
            
#         return profit
    
        