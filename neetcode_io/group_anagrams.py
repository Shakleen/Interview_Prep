from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for str in strs:
            counter = [0 for _ in range(26)]

            for ch in str:
                counter[ord(ch) - ord('a')] += 1

            output[tuple(counter)].append(str)

        return output.values()


if __name__ == "__main__":
    solution = Solution()

    print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
    print(solution.groupAnagrams(["x"]))
    print(solution.groupAnagrams([""]))