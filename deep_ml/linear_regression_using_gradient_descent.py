import numpy as np


def linear_regression_gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    alpha: float,
    iterations: int,
) -> np.ndarray:
    m, n = X.shape
    theta = np.zeros((n, 1))
    y = y.reshape(-1, 1)
    
    for _ in range(iterations):
        y_hat = X @ theta
        error = y_hat - y
        grad = X.T @ error / m
        theta -= alpha * grad

    return np.round(theta.flatten(), 4)


if __name__ == "__main__":
    print(
        linear_regression_gradient_descent(
            X=np.array([[1, 1], [1, 2], [1, 3]]),
            y=np.array([1, 2, 3]),
            alpha=0.01,
            iterations=1000,
        )
    )
