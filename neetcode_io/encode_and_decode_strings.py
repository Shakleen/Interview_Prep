from typing import List


class Solution:
    delim = "#" * 3

    def encode(self, strs: List[str]) -> str:
        s = "".join(str(len(s)) + Solution.delim + s for s in strs)
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        idx = 0
        num = ""

        while idx < len(s):
            if "0" <= s[idx] <= "9":
                num += s[idx]
                idx += 1
            elif s[idx] == '#':
                num = int(num)
                strs.append(s[idx + len(Solution.delim) : idx + num + len(Solution.delim)])
                idx += num + len(Solution.delim)
                num = ""


        return strs


if __name__ == "__main__":
    test_cases = [
        {"strs": ["neet", "code", "love", "you"]},
        {"strs": ["we", "say", ":", "yes"]},
        {"strs": ["", "", "", ""]}
    ]

    solution = Solution()

    for tc in test_cases:
        tc["encoded"] = solution.encode(tc["strs"])
        tc["decoded"] = solution.decode(tc["encoded"])

        print(tc)
