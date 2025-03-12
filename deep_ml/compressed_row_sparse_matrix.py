import numpy as np


def compressed_row_sparse_matrix(dense_matrix):
    """
    Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

    :param dense_matrix: 2D list representing a dense matrix
    :return: A tuple containing (values array, column indices array, row pointer array)
    """
    values_array = []
    column_indices = []
    row_pointers = [0]

    for row in dense_matrix:
        row_counter = row_pointers[-1]

        for col_idx, val in enumerate(row):
            if not val:
                continue

            values_array.append(val)
            column_indices.append(col_idx)
            row_counter += 1

        row_pointers.append(row_counter)

    return values_array, column_indices, row_pointers


if __name__ == "__main__":
    dense_matrix = [[1, 0, 0, 0], [0, 2, 0, 0], [3, 0, 4, 0], [1, 0, 0, 5]]

    vals, col_idx, row_ptr = compressed_row_sparse_matrix(dense_matrix)
    print("Values array:", vals)
    print("Column indices array:", col_idx)
    print("Row pointer array:", row_ptr)
