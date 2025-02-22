import numpy as np


def dice_score(y_true, y_pred):
    intersection = np.sum((y_true == 1) & (y_pred == 1))
    denom = (np.sum(y_true == 1) + np.sum(y_pred == 1))

    if denom:
        res = 2 * intersection / denom
        return round(res, 3)
    return 0.0


if __name__ == "__main__":
    y_true = np.array([1, 1, 0, 1, 0, 1])
    y_pred = np.array([1, 1, 0, 0, 0, 1])
    print(dice_score(y_true, y_pred))
