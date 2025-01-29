def matrix_dot_vector(matrix, vector):
    if len(matrix[0]) != len(vector):
        return -1

    result = [sum(a * b for a, b in zip(row, vector)) for row in matrix]

    return result


if __name__ == "__main__":
    a = [[1, 2], [2, 4]]
    b = [1, 2]

    print(matrix_dot_vector(a, b))

    a = [[1, 2], [2, 4]]
    b = [1, 2, 3]
    print(matrix_dot_vector(a, b))
