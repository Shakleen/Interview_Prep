import numpy as np


def linear_regression_normal_equation(
    X: list[list[float]], y: list[float]
) -> list[float]:
    X, y = np.array(X), np.array(y)
    a = np.dot(X.T, X)
    a_inv = np.linalg.inv(a)
    output = np.dot(np.dot(a_inv, X.T), y)
    return list(map(lambda x: round(x, 4), output.tolist()))


if __name__ == "__main__":
    print(
        linear_regression_normal_equation(
            X=[[1, 1], [1, 2], [1, 3]],
            y=[1, 2, 3],
        )
    )
