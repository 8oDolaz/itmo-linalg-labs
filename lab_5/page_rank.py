import warnings
warnings.filterwarnings("ignore")

import numpy as np


def matrix_from_txt(filename: str) -> list[list[float]]:
    with open(filename, 'r') as matrix:
        matrix = matrix.read()
        return [
            [float(val) for val in row.replace(' ', '').split(',')]
            for row in matrix.split('\n')
        ]


def normalize_to_radius(
        vector: np.ndarray,
        radius_min: int = 20, 
        radius_max: int = 100) -> np.ndarray:
    vector = (vector - vector.min()) / (vector.max() - vector.min())
    vector = vector * (radius_max - radius_min) + radius_min

    return vector


def markov_from_adjacency(adjacency: np.matrix) -> np.matrix:
    markov = np.matrix(np.zeros(adjacency.shape))
    for j in range(len(adjacency)):
        total_edges_j = adjacency[j, :].sum()

        if not total_edges_j:
            markov[j, j] = 1
            continue

        for i in range(len(adjacency)):
            markov[i, j] = adjacency[j, i] / total_edges_j

    return markov


def main():
    adjacency_matrix = np.matrix(matrix_from_txt('adjacency_matrix.txt'))
    transition_matrix = markov_from_adjacency(adjacency_matrix)

    eigen_values, eigen_vectors = np.linalg.eig(transition_matrix)
    converge_vector = np.hstack([
        eigen_vectors[:, i] / eigen_vectors[:, i].sum()
        for i in range(len(transition_matrix))
        if np.isclose(np.absolute(eigen_values[i]), 1)
    ])
    converge_vector = converge_vector.real
    print(np.round(converge_vector, 2))

    verticies_ranked = sorted(
        range(1, len(converge_vector) + 1),
        key=lambda i: converge_vector[i - 1, 0],
        reverse=True
    )
    print(verticies_ranked)

    print(np.round(converge_vector * 100, 1))
    converge_vector = normalize_to_radius(converge_vector)
    print(np.round(converge_vector))


if __name__ == '__main__':
    main()
