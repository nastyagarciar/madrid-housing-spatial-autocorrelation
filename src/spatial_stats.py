"""Spatial-autocorrelation utilities for the Madrid housing project."""

from __future__ import annotations

import numpy as np
from sklearn.neighbors import NearestNeighbors


EARTH_RADIUS_KM = 6371.0088


def knn_indices(latitude, longitude, k=8):
    """Return k-nearest-neighbor indices using haversine distance."""
    coordinates = np.radians(
        np.column_stack([latitude, longitude]).astype(float)
    )

    nn = NearestNeighbors(
        n_neighbors=k + 1,
        metric="haversine",
        algorithm="ball_tree",
    )
    nn.fit(coordinates)

    distances, indices = nn.kneighbors(coordinates)
    return indices[:, 1:], distances[:, 1:]


def moran_i(values, neighbor_indices):
    """Compute global Moran's I with equal row-standardized kNN weights."""
    values = np.asarray(values, dtype=float)
    z = values - values.mean()

    spatial_lag = z[neighbor_indices].mean(axis=1)
    denominator = np.sum(z ** 2)

    observed = np.sum(z * spatial_lag) / denominator
    return float(observed), z, spatial_lag


def permutation_test(
    values,
    neighbor_indices,
    permutations=999,
    seed=42,
):
    """Two-sided permutation test for global Moran's I."""
    observed, _, _ = moran_i(values, neighbor_indices)

    rng = np.random.default_rng(seed)
    simulated = np.empty(permutations, dtype=float)

    for i in range(permutations):
        simulated[i] = moran_i(
            rng.permutation(values),
            neighbor_indices,
        )[0]

    p_value = (
        np.sum(np.abs(simulated) >= abs(observed)) + 1
    ) / (permutations + 1)

    return observed, float(p_value), simulated
