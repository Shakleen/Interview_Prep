import numpy as np


def cross_validation_split(data: np.ndarray, k: int, seed=42) -> list:
    np.random.seed(seed)

    data = data.tolist()
    indices = np.arange(len(data))
    np.random.shuffle(indices)

    folds = []
    split_size = len(data) // k

    for i in range(k):
        train_fold = []
        test_fold = []

        for j, row in enumerate(data):
            if j // split_size == i:
                test_fold.append(row)
            else:
                train_fold.append(row)

        folds.append([train_fold, test_fold])

    return folds


if __name__ == "__main__":
    # print(
    #     cross_validation_split(
    #         data=np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]),
    #         k=5,
    #     )
    # )

    print(
        cross_validation_split(
            data=np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]),
            k=5,
        )
    )
