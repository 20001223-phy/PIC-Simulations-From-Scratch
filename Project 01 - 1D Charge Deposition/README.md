# Project 01 — 1D Charge Deposition Using Cloud-in-Cell (CIC)

## Overview

This project implements a basic one-dimensional charge deposition algorithm used in Particle-in-Cell (PIC) simulations.

In PIC simulations, particles move continuously through space, while electromagnetic field quantities are calculated on a computational grid. Charge deposition transfers particle charge onto nearby grid points so that the charge distribution can later be used in field calculations.

## Objectives

- Construct a one-dimensional computational grid.
- Define particle positions independently of grid points.
- Identify the neighboring grid points for each particle.
- Calculate Cloud-in-Cell (CIC) weighting factors.
- Distribute particle charge between neighboring grid points.
- Accumulate the deposited charge on the grid.

## Method

The Cloud-in-Cell method distributes each particle's charge between its two neighboring grid points according to its position.

For a particle located between grid points \(x_i\) and \(x_{i+1}\), the weighting factors are:

\[
w_i=\frac{x_{i+1}-x_p}{\Delta x}
\]

\[
w_{i+1}=\frac{x_p-x_i}{\Delta x}
\]

The charge contributions are:

\[
q_i=q_p w_i,\qquad q_{i+1}=q_p w_{i+1}
\]

The weights satisfy:

\[
w_i+w_{i+1}=1
\]

This ensures that the total particle charge is conserved during deposition.

## Simulation Parameters

- Domain: \(0 \leq x \leq 10\)
- Number of grid points: 11
- Grid spacing: 1
- Number of particles: 3
- Particle positions: 2.3, 5.7, 8.4
- Particle charge: \(-1.602\times10^{-19}\,\mathrm{C}\) per particle

## Results

The simulation produces three visualizations:

1. One-dimensional computational grid.
2. Particle positions relative to the grid.
3. Final charge distribution deposited onto the grid.

## Tools and Libraries

- Python
- NumPy
- Matplotlib

## Learning Outcome

This project demonstrates the charge deposition stage of a basic PIC algorithm using the Cloud-in-Cell method. It provides a foundation for subsequent PIC steps, including charge-density calculation, solving Poisson's equation, and particle-field interaction.

## Project Status

Completed — basic one-dimensional CIC charge deposition.
