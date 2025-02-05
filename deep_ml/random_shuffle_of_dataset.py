import numpy as np


def shuffle_data(X, y, seed=None):
    np.random.seed(seed)

    indices = np.arange(len(X))
    np.random.shuffle(indices)

    X_out, y_out = [None for _ in indices], [None for _ in indices]

    for i, idx in enumerate(indices):
        X_out[i] = X[idx]
        y_out[i] = y[idx]

    return X_out, y_out


if __name__ == "__main__":
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y = np.array([1, 2, 3, 4])

    print(shuffle_data(X, y, seed=1))
    print(shuffle_data(X, y, seed=1))
    print(shuffle_data(X, y, seed=2))