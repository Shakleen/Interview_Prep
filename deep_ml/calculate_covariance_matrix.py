def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    mean_matrix = [sum(vector) / len(vector) for vector in vectors]
    sub_matrix = [
        [val - mean_matrix[i] for val in vector] 
        for i, vector in enumerate(vectors)
    ]

    N_ROWS, N_COLS = len(sub_matrix), len(sub_matrix[0])
    cov_matrix = [[0 for _ in range(N_ROWS)] for _ in range(N_ROWS)]

    for i in range(N_ROWS):
        for j in range(N_ROWS):
            cov_matrix[i][j] = sum(
                sub_matrix[i][k] * sub_matrix[j][k] for k in range(N_COLS)
            ) / (N_COLS - 1)

    return cov_matrix


if __name__ == "__main__":
    print(calculate_covariance_matrix([[1, 2, 3], [4, 5, 6]]))
