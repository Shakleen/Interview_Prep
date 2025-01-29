class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = [0 for _ in range(26)]

        for c in s:
            counter[ord(c) - ord('a')] += 1

        for c in t:
            counter[ord(c) - ord('a')] -= 1

        return not any(counter)
    

if __name__ == "__main__":
    solution = Solution()

    print(solution.isAnagram('racecar', 'carrace'))
    print(solution.isAnagram('jar', 'jam'))
    print(solution.isAnagram('', ''))
    print(solution.isAnagram('', 'a'))