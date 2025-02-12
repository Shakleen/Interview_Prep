from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1

        while lo != hi:
            sum = numbers[lo] + numbers[hi]

            if sum == target:
                return [lo + 1, hi + 1]
            elif sum > target:
                hi -= 1
            else:
                lo += 1


if __name__ == "__main__":
    test_cases = [
        {"numbers": [1, 2, 3, 4], "target": 3, "expected": [1, 2]},
        {"numbers": [1, 2, 3, 5], "target": 5, "expected": [2, 3]},
        {"numbers": [1, 2], "target": 3, "expected": [1, 2]},
    ]
    solution = Solution()

    for tc in test_cases:
        tc["actual"] = solution.twoSum(tc["numbers"], tc["target"])
        tc["passed"] = tc["actual"] == tc["expected"]
        print(tc["passed"])
