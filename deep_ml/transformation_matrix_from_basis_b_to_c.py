import numpy as np


def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    return np.round(np.linalg.inv(np.array(C)) @ np.array(B), 4).tolist()


if __name__ == "__main__":
    B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    C = [[1, 2.3, 3], [4.4, 25, 6], [7.4, 8, 9]]
    print(transform_basis(B, C))
