def transpose_matrix(matrix: list[list[int|float]]) -> list[list[int|float]]:
    N_COLS = len(matrix[0])
    output = [[] for _ in range(N_COLS)]

    for row in matrix:
        for i, val in enumerate(row):
            output[i].append(val)

    return output


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    print(transpose_matrix(a))

    a = [[1]]
    print(transpose_matrix(a))

    a = [[1, 2, 3]]
    print(transpose_matrix(a))
