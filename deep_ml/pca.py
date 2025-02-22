import numpy as np


def pca(data: np.ndarray, k: int) -> np.ndarray:
    mean_data = np.mean(data, axis=0, keepdims=True)
    std_data = np.std(data, axis=0, keepdims=True)
    P = (data - mean_data) / std_data

    cov = np.cov(P, rowvar=False)

    values, vectors = np.linalg.eig(cov)

    sorted_indices = np.argsort(values)[::-1]
    sorted_values = values[sorted_indices]
    sorted_vectors = vectors[:, sorted_indices]

    principal_components = sorted_vectors[:, :k]
    return np.round(principal_components, 4).tolist()


if __name__ == "__main__":
    print(pca(np.array([[4, 2, 1], [5, 6, 7], [9, 12, 1], [4, 6, 7]]), 2))

    # from sklearn.decomposition import PCA
