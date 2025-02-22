import numpy as np


def jaccard_index(y_true, y_pred):
    intersection = np.sum((y_true == 1) & (y_pred == 1))
    union = np.sum((y_true == 1) | (y_pred == 1))
    result = intersection / union
    if np.isnan(result):
        return 0.0
    return round(result, 3)


if __name__ == "__main__":
    y_true = np.array([1, 0, 1, 1, 0, 1])
    y_pred = np.array([1, 0, 1, 0, 0, 1])
    # y_true = np.zeros_like(y_pred)
    y_pred = np.zeros_like(y_true)
    print(jaccard_index(y_true, y_pred))
