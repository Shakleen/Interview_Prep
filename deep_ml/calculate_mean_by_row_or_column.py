def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    N_ROWS, N_COLS = len(matrix), len(matrix[0])

    if mode == "column":
        output = [
            sum(matrix[i][j] for i in range(N_ROWS)) / N_COLS for j in range(N_COLS)
        ]
    else:
        output = [
            sum(matrix[i][j] for j in range(N_COLS)) / N_COLS for i in range(N_ROWS)
        ]

    return output


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(calculate_matrix_mean(matrix, "column"))
    print(calculate_matrix_mean(matrix, "row"))
