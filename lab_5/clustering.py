import warnings
warnings.filterwarnings("ignore")

import argparse
from pprint import pprint
from collections import defaultdict

import numpy as np
from sklearn.cluster import KMeans


def matrix_from_txt(filename: str) -> list[list[int]]:
    with open(filename, 'r') as matrix:
        matrix = matrix.read()
        return [
            [int(val) for val in row.replace(' ', '').split(',')]
            for row in matrix.split('\n')
        ]


def get_clusters(points: np.ndarray) -> np.ndarray:
    k_means = KMeans(n_clusters=k)

    points = np.squeeze(np.asarray(points))
    kmeans = k_means.fit(points)

    return kmeans.labels_


def group_by_clusters(clusters: list) -> dict:
    groups = defaultdict(list)
    for vertex, cluster in enumerate(clusters):
        groups[cluster + 1].append(vertex + 1)

    return dict(groups)


def main():
    incidence_matrix = matrix_from_txt('incidence_matrix_1.txt')
    incidence_matrix = np.matrix(incidence_matrix)

    laplacian_matrix = incidence_matrix * incidence_matrix.T

    eigen_values, eigen_vectors = np.linalg.eig(laplacian_matrix)
    eigen = [
        (eigen_values[i], eigen_vectors[:, i])
        for i in range(len(eigen_values))
    ]
    eigen = sorted(eigen, key=lambda x: x[0])

    cluster_matrix = eigen[0][1]
    for _, e_vec in eigen[1:k]:
        cluster_matrix = np.hstack((cluster_matrix, e_vec))

    clusters = get_clusters(cluster_matrix).tolist()
    clusters = group_by_clusters(clusters)

    pprint(clusters)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-k', 
        default=4, type=int, help='Number of clusters'
    )
    k = parser.parse_args().k

    main()
