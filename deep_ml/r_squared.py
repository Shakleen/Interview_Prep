import numpy as np


def r_squared(y_true, y_pred):
    # Write your code here
    ssr_median = np.sum((y_true - np.median(y_true)) ** 2)
    ssr_model = np.sum((y_pred - y_true) ** 2)
    return np.round((ssr_median - ssr_model) / ssr_median, 3)


if __name__ == "__main__":
    y_true = np.array([1, 2, 3, 4, 5])
    y_pred = np.array([1.1, 2.1, 2.9, 4.2, 4.8])
    print(r_squared(y_true, y_pred))
