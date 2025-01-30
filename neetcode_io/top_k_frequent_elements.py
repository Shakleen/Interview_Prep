from typing import List
from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        reverse_counter = defaultdict(list)

        for val, freq in counter.items():
            reverse_counter[freq].append(val)

        output = []

        for freq in sorted(reverse_counter.keys(), reverse=True):
            output.extend(reverse_counter[freq])

            if len(output) == k:
                break

        return output


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {"nums": [1, 2, 2, 3, 3, 3], "k": 2},
        {"nums": [7, 7], "k": 1},
        {"nums": [7, 7, 9, 9], "k": 2},
    ]

    for test_case in test_cases:
        test_case["result"] = solution.topKFrequent(**test_case)
        print(test_case)