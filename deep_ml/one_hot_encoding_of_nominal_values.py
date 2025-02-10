import numpy as np


def to_categorical(x, n_col=None):
    max_val = np.max(x)
    output = np.zeros((len(x), max_val + 1))
    output[np.arange(len(x)), x] = 1
    output = output.astype(np.float32)
    return output.tolist()


if __name__ == "__main__":
    print(to_categorical(np.array([0, 0])))
    print(to_categorical(np.array([0, 1])))
    print(to_categorical(np.array([1])))
    print(to_categorical(np.array([0, 1, 2, 1, 0])))
    print(to_categorical(np.array([0, 1, 2, 1, 3])))
    print(to_categorical(np.array([0, 1, 2, 1, 4])))
    print(to_categorical(np.array([0, 1, 2, 3, 4])))
