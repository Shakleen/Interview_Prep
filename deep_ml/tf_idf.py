import numpy as np


def count_occurrences(doc, word):
    return sum(w == word for w in doc)


def count_presences(corpus, word):
    return sum(word in doc for doc in corpus)


def compute_tf_idf(corpus, query):
    """
    Compute TF-IDF scores for a query against a corpus of documents.

    :param corpus: List of documents, where each document is a list of words
    :param query: List of words in the query
    :return: List of lists containing TF-IDF scores for the query words in each document
    """
    Q, D = len(query), len(corpus)

    if D == 0:
        raise Exception

    tf = np.zeros((D, Q))
    idf = np.zeros((D, Q))

    for i, doc in enumerate(corpus):
        for j, word in enumerate(query):
            tf[i][j] = count_occurrences(doc, word) / len(doc)
            idf[i][j] = np.log((1 + D) / (1 + count_presences(corpus, word))) + 1

    tf_idf = tf * idf
    return np.round(tf_idf, 5).tolist()


if __name__ == "__main__":
    print(
        compute_tf_idf(
            corpus=[
                ["the", "cat", "sat", "on", "the", "mat"],
                ["the", "dog", "chased", "the", "cat"],
                ["the", "bird", "flew", "over", "the", "mat"],
            ],
            query=["cat"],
        )
    )
