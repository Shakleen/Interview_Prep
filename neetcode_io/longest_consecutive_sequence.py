from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                
                while (num + length) in numSet:
                    length += 1
                
                longest = max(length, longest)

        return longest


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        {"nums": [2, 20, 4, 10, 3, 4, 5], "expected": 4},
        {"nums": [0, 3, 2, 5, 4, 6, 1, 1], "expected": 7},
        {"nums": [], "expected": 0},
        {"nums": [0], "expected": 1},
    ]

    for tc in test_cases:
        tc["actual"] = solution.longestConsecutive(tc["nums"])
        tc["result"] = tc["actual"] == tc["expected"]
        print(tc["result"])
