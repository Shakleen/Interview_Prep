from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            min_height = min(heights[l], heights[r])
            distance = r - l
            area = min_height * distance
            max_area = max(max_area, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_area


if __name__ == "__main__":
    test_cases = [
        {"heights": [1, 7, 2, 5, 4, 7, 3, 6], "expected": 36},
        {"heights": [2, 2, 2], "expected": 4},
    ]
    solution = Solution()

    for tc in test_cases:
        tc["actual"] = solution.maxArea(tc["heights"])
        tc["passed"] = tc["actual"] == tc["expected"]
        print(tc)
