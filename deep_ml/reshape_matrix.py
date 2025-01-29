import numpy as np

def reshape_matrix(matrix: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    return np.reshape(a, new_shape).tolist()


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    print(reshape_matrix(a, (3, 2)))
