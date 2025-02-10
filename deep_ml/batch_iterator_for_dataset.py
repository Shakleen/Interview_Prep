import numpy as np


def batch_iterator(X, y=None, batch_size=64):
	batches = []

	for i in range(0, len(X), batch_size):
		batch = [X[i : i + batch_size].tolist()]

		if y is not None:
			batch.append(y[i : i + batch_size].tolist())
		
		batches.append(batch)

	return batches
    


if __name__ == "__main__":
    print(batch_iterator(
        np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8], 
                  [9, 10]]),
		np.array([1, 2, 3, 4, 5]),
		batch_size=2,
	))
    print(batch_iterator(
        np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8], 
                  [9, 10]]),
		# np.array([1, 2, 3, 4, 5]),
		batch_size=2,
	))