from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {"nums": [1, 2, 4, 8]},
        {"nums": [-1, 0, 1, 2, 3]},
        {"nums": [1, 0]},
        {"nums": [-1, 0]},
        {"nums": [1, -1]},
    ]


    for tc in test_cases:
        tc["result"] = solution.productExceptSelf(**tc)
        print(tc)