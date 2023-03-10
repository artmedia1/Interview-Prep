from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = 0
        rp = 1
        maxProfit = 0
        while rp < len(prices):
            currProfit = prices[rp] - prices[lp]
            if prices[lp] < prices[rp]:
                maxProfit = max(maxProfit, currProfit)
            else:
                lp = rp

            rp += 1

        return maxProfit

if __name__ == "__main__":
    solution = Solution()
    prices = [7,1,5,3,6,4]
    test = solution.maxProfit(prices)
    print(test)