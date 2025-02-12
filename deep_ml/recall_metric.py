import numpy as np


def recall(y_true, y_pred):
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    return np.round(tp / (tp + fn), 3)


if __name__ == "__main__":
    print(
        recall(
            np.array([1, 0, 1, 1, 0, 1]),
            np.array([1, 0, 1, 0, 0, 1]),
        )
    )
