from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for i, num in enumerate(nums):
            remaining = target - num

            if remaining in tracker:
                return [tracker[remaining], i]

            tracker[num] = i

        return [0, 0]


if __name__ == "__main__":
    solution = Solution()

    print(solution.twoSum([3, 4, 5, 6], 7))
    print(solution.twoSum([4, 5, 6], 10))
    print(solution.twoSum([5, 5], 10))
