import math


def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:
    a = 1
    b = matrix[0][0] + matrix[1][-1]
    c = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    output = [
        (b + math.sqrt(b**2 - 4 * a * c)) / (2 * a),
        (b - math.sqrt(b**2 - 4 * a * c)) / (2 * a),
    ]
    return sorted(output, reverse=True)


if __name__ == "__main__":
    print(calculate_eigenvalues([[2, 1], [1, 2]]))
