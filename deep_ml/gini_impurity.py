import numpy as np


def gini_impurity(y):
    """
    Calculate Gini Impurity for a list of class labels.

    :param y: List of class labels
    :return: Gini Impurity rounded to three decimal places
    """
    unique_classes = set(y)
    val = 1
    y = np.array(y)

    for c in unique_classes:
        val -= (np.sum(y == c) / len(y)) ** 2

    return round(val, 3)


if __name__ == "__main__":
    y = [0, 1, 1, 1, 0]
    print(gini_impurity(y))