import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z0-9]", "", s).lower()
        
        lo, hi = 0, len(s)-1

        while lo <= hi:
            if s[lo] != s[hi]:
                return False
            
            lo += 1
            hi -= 1

        return True


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        {"s": "Was it a car or a cat I saw?", "expected": True},
        {"s": "tab a cat", "expected": False},
        {"s": "t", "expected": True},
        {"s": "tt", "expected": True},
        {"s": "tTt", "expected": True},
    ]

    for tc in test_cases:
        tc["actual"] = solution.isPalindrome(tc["s"])
        tc["result"] = tc["actual"] == tc["expected"]
        print(tc["result"])
