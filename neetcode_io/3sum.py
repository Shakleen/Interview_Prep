from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()

        for i, num in enumerate(nums):
            j = i + 1
            k = len(nums) - 1
            target = (-1) * num

            while j < k:
                sum = nums[j] + nums[k]

                if target == sum:
                    output.add((num, nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum > target:
                    k -= 1
                else:
                    j += 1
        

        return [list(o) for o in output]


if __name__ == "__main__":
    test_cases = [
        {"nums": [-1, 0, 1, 2, -1, -4], "expected": [[-1, -1, 2], [-1, 0, 1]]},
        {"nums": [0, 1, 1], "expected": []},
        {"nums": [0, 0, 0], "expected": [[0, 0, 0]]},
    ]

    solution = Solution()

    for tc in test_cases:
        tc["actual"] = solution.threeSum(tc["nums"])
        tc["passed"] = tc["actual"] == tc["expected"]
        print(tc)
