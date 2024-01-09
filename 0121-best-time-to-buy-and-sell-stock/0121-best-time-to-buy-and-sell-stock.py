class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        answer = 0
            
        for price in prices:
            if price < min_price:
                min_price = price
            
            answer = max(price - min_price, answer)
            
        return answer