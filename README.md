# borehole-log-alignment
Object-oriented Python project for borehole log alignment based on clustering of gamma-ray values and depth-shift correlation.

## Problem context
Borehole logs recorded at different times or with different tools often exhibit
systematic depth offsets. Accurate depth alignment is critical for log
correlation, reservoir characterization, and well-to-well comparisons.

## Method overview
1. Load and clean gamma-ray logs from LAS files
2. Cluster GR values using a custom 1D K-means implementation
3. Convert clusters to categorical labels
4. Estimate the optimal vertical depth shift (Δz) by maximizing label similarity

## Example output

Gamma-ray log alignment before and after depth shifting.

![GR log alignment](figures/printfigure.png)
