class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        tracker = set()
        left = 0
        tracker.add(s[left])
        max_count = 1
        count = 1

        for right in range(1, len(s)):
            while s[right] in tracker:
                tracker.remove(s[left])
                left += 1
                count -= 1

            tracker.add(s[right])
            count += 1
            max_count = max(max_count, count)

        return max_count


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        {"s": "zxyzxyz", "expected": 3},
        {"s": "xxxx", "expected": 1},
        {"s": "", "expected": 0},
        {"s": "abcde", "expected": 5},
        {"s": "ab" * 500, "expected": 2},
        {"s": " ", "expected": 1},
    ]

    for tc in test_cases:
        tc["actual"] = solution.lengthOfLongestSubstring(tc["s"])
        tc["result"] = tc["actual"] == tc["expected"]
        print(tc["result"])
