def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    result = [
        [val * scalar for val in row]
        for row in matrix
    ]

    return result


if __name__ == "__main__":
    for i in range(4):
        print(scalar_multiply(
            matrix=[[1, 2], [3, 4]],
            scalar=i
        ))