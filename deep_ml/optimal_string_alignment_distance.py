def OSA(source: str, target: str) -> int:
    N_ROWS, N_COLS = len(source), len(target)
    dp = [[0 for _ in range(N_COLS + 1)] for _ in range(N_ROWS + 1)]

    for i in range(1, N_ROWS + 1):
        dp[i][0] = i
        
    for j in range(1, N_COLS + 1):
        dp[0][j] = j

    for i in range(1, N_ROWS + 1):
        for j in range(1, N_COLS + 1):
            min_val = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
            dp[i][j] = min_val + int(source[i - 1] != target[j - 1])

    return dp[-1][-1]


if __name__ == "__main__":
    print(OSA(source="butterfly", target="dragonfly"))
