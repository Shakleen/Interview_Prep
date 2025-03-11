from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0

        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)

            if prices[right] < prices[left]:
                left = right

        return max_profit


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        {"prices": [10, 1, 5, 6, 7, 1], "expected": 6},
        {"prices": [10, 8, 7, 5, 2], "expected": 0},
        {"prices": [8], "expected": 0},
    ]

    for tc in test_cases:
        tc["actual"] = solution.maxProfit(tc["prices"])
        tc["result"] = tc["actual"] == tc["expected"]
        print(tc["result"])
