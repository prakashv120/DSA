class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maximum=0
        minimum=float('inf')
        for price in prices:
            minimum=min(minimum,price)
            maximum=max(price-minimum,maximum)
        return maximum

        