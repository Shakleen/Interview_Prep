import numpy as np


def log_softmax(scores: list) -> np.ndarray:
    scores -= np.max(scores)
    exp = np.exp(scores)
    sum = np.sum(exp)
    return np.round(scores - np.log(sum), 4)


if __name__ == "__main__":
    print(log_softmax(np.array([1, 2, 3])))
