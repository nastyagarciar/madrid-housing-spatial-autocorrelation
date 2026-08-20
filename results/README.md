# Results

## Main result — 8-nearest-neighbor weights

| Metric | Raw Price | Log Price |
|---|---:|---:|
| Moran's I | 0.2766 | 0.2961 |
| Permutation p-value | 0.001 | 0.001 |

The positive Moran's I indicates that nearby properties tend to have more similar prices than expected under spatial randomness.

## Sensitivity

The result is stable across k-nearest-neighbor specifications from 4 to 20 neighbors.

## Moran quadrants

- Low-Low: 1318
- High-High: 1177
- High-Low: 610
- Low-High: 528

These are exploratory quadrant labels based on standardized log price and spatial lag, not significance-filtered Local Moran clusters.
