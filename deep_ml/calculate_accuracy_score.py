import numpy as np

def accuracy_score(y_true, y_pred):
    matches = np.sum(y_true == y_pred)
    return matches / len(y_true)


if __name__ == "__main__":
    y_true = np.array([1, 0, 1, 1, 0, 1])
    y_pred = np.array([1, 0, 0, 1, 0, 1])
    output = accuracy_score(y_true, y_pred)
    print(output)