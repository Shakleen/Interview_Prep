from math import sqrt


def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def find_centroid_no(centroids, point):
    min_dist = 1e10
    min_idx = -1

    for idx, centroid in enumerate(centroids):
        dist = distance(centroid, point)

        if dist < min_dist:
            min_dist = dist
            min_idx = idx

    return min_idx


def find_centroid_numbers(points, final_centroids, centroid_numbers):
    for i, point in enumerate(points):
        centroid_numbers[i] = find_centroid_no(final_centroids, point)


def update_centroids(points, k, final_centroids, cluster_numbers):
    for i in range(k):
        counter = 0
        coords = [0 for _ in range(len(points[0]))]

        for j, cluster_no in enumerate(cluster_numbers):
            if cluster_no == i:
                point = points[j]

                for k, p in enumerate(point):
                    coords[k] += p

                counter += 1

        coords = [round(x / counter, 4) for x in coords]
        final_centroids[i] = coords


def k_means_clustering(
    points: list[tuple[float, float]],
    k: int,
    initial_centroids: list[tuple[float, float]],
    max_iterations: int,
) -> list[tuple[float, float]]:
    # What point belongs to what cluster
    # Calculate cluster mean
    # Find updated centroid
    # Repeat above steps
    final_centroids = [c for c in initial_centroids]
    centroid_numbers = [0 for _ in points]

    for _ in range(max_iterations):
        find_centroid_numbers(points, final_centroids, centroid_numbers)
        update_centroids(points, k, final_centroids, centroid_numbers)

    return final_centroids


print(
    k_means_clustering(
        points=[(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)],
        k=2,
        initial_centroids=[(1, 1), (10, 1)],
        max_iterations=10,
    )
)

print(
    k_means_clustering(
        [(0, 0, 0), (2, 2, 2), (1, 1, 1), (9, 10, 9), (10, 11, 10), (12, 11, 12)],
        2,
        [(1, 1, 1), (10, 10, 10)],
        10,
    )
)
