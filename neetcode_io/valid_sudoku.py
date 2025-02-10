from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c == ".":
                    continue

                idx = 3 * (i // 3) + (j // 3)

                if c in row[i] or c in column[j] or c in grid[idx]:
                    return False
                
                row[i].add(c)
                column[j].add(c)
                grid[idx].add(c)

        return True


if __name__ == "__main__":
    test_cases = [
        {
            "board": [
                ["1", "2", ".", ".", "3", ".", ".", ".", "."],
                ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", ".", "3"],
                ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", ".", ".", ".", ".", ".", "2", ".", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            "expected": True,
        },
        {
            "board": [
                ["1", "2", ".", ".", "3", ".", ".", ".", "."],
                ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                [".", "9", "1", ".", ".", ".", ".", ".", "3"],
                ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", ".", ".", ".", ".", ".", "2", ".", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            "expected": False,
        },
    ]

    solution = Solution()

    for tc in test_cases:
        tc["actual"] = solution.isValidSudoku(tc["board"])
        tc["passed"] = tc["actual"] == tc["expected"]
        print("Passed", tc["passed"], "Actual", tc["actual"], "Expected", tc["expected"])
