# Project 02 — 1D Charge Density Calculation

## Overview

This project calculates and visualizes the one-dimensional charge density from a predefined distribution of deposited grid charges.

It introduces the conversion of discrete grid charge values into a charge-density distribution, an important step in electrostatic Particle-in-Cell (PIC) simulations.

## Objectives

- Define a one-dimensional computational grid.
- Specify deposited charge values at grid points.
- Calculate charge density.
- Verify charge conservation.
- Visualize the charge-density distribution.

## Mathematical Background

Charge density is defined as:

\[
\rho = \frac{Q}{V}
\]

For this simplified one-dimensional model, assuming a unit cross-sectional area:

\[
\rho_j = \frac{Q_j}{\Delta x}
\]

where:

- \(\rho_j\): Charge density
- \(Q_j\): Deposited grid charge
- \(\Delta x\): Grid spacing

The charge density is expressed in C/m³.

## Computational Method

1. Define the computational domain and grid spacing.
2. Specify the deposited grid charges.
3. Calculate charge density at each grid point.
4. Calculate the total charge from the density distribution.
5. Check charge conservation.
6. Plot the charge-density distribution.

## Results

The simulation produces a charge-density distribution across the computational grid.

The negative charge-density values result from the negative charges assigned to the grid points.

The charge conservation check verifies that the total charge reconstructed from the density agrees with the original grid charge.

## Visualization

The charge-density distribution is plotted using Matplotlib.

## Tools and Libraries

- Python
- NumPy
- Matplotlib

## How to Run

```bash
python charge_density.py
```

## Learning Outcome

This project demonstrates how deposited grid charges can be converted into charge density, preparing for the numerical solution of Poisson's equation in subsequent PIC projects.

## Next Project

**Project 03 — 1D Poisson Solver**

The next project will explore calculating electric potential from a charge-density distribution by numerically solving Poisson's equation.
