import numpy as np


def make_diagonal(x):
    output = np.zeros((len(x), len(x))).astype(np.float32)
    indices = np.arange(len(x))
    output[indices, indices] = x
    return output.tolist()


if __name__ == "__main__":
    print(make_diagonal(np.array([1])))
    print(make_diagonal(np.array([1, 2])))
    print(make_diagonal(np.array([1, 2, 3])))
    print(make_diagonal(np.array([1, 2, 3, 4])))
