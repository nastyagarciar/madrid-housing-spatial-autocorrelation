# Methodology

## Objective

Quantify spatial autocorrelation in housing prices within Madrid's historical centre.

The source task specifically asks for the historical-centre subset and the variables:

- `house.price`
- `historical`
- `longitude`
- `latitude`

## Sample

- Full Madrid dataset: **10,512**
- Historical-centre properties used: **3,633**

No missing values remain in price or coordinates after validation.

## Spatial weights

The primary analysis uses **8-nearest-neighbor (8-NN)** weights.

Coordinates are converted to radians and nearest neighbors are determined using **haversine distance**.

Each observation assigns equal weight `1/k` to its k nearest neighbors, producing a row-standardized weight matrix.

Mean 8-neighbor distance: **0.131 km**

## Moran's I

Global Moran's I is computed for:

1. raw housing price;
2. log housing price.

The primary log-price result is:

- Moran's I: **0.2961**
- permutation p-value: **0.001**

A 999-permutation two-sided test evaluates whether the observed spatial pattern is compatible with spatial randomness.

## Robustness

The analysis repeats Moran's I for `k = 4, 8, 12, 20`.

All specifications remain positive:

- Raw price: **0.248 to 0.295**
- Log price: **0.271 to 0.319**

This reduces dependence on a single arbitrary neighborhood definition.

## Moran quadrants

High-High and Low-Low labels describe the sign of each standardized log price and its local spatial lag.

They are useful exploratory categories, but this repository does **not** label them statistically significant local clusters because a full local-permutation significance correction is outside the scope of the project.
