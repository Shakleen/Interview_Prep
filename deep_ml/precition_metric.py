import numpy as np


def precision(y_true, y_pred):
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    return tp / (tp + fp)


if __name__ == "__main__":
    print(
        precision(
            np.array([1, 0, 1, 1, 0, 1]),
            np.array([1, 0, 1, 0, 0, 1]),
        )
    )
