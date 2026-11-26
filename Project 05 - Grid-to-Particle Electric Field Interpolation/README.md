
# Project 05 — Grid-to-Particle Electric Field Interpolation

## Objective
Interpolate the electric field from computational grid nodes to particle positions using linear interpolation.

## Description
In Particle-In-Cell (PIC) simulations, electric fields are calculated on a computational grid, while particles can occupy positions between grid nodes.

This project implements grid-to-particle electric field interpolation in one dimension. A Gaussian electrostatic potential is defined on the grid, and its electric field is calculated numerically. The electric field at selected particle positions is then obtained using linear interpolation.

Interpolated values are compared with the analytical electric field to estimate interpolation error.

## Method
- Define a one-dimensional computational grid.
- Calculate the electrostatic potential.
- Calculate the electric field on grid nodes using finite differences.
- Define particle positions between grid nodes.
- Interpolate the grid electric field to particle positions.
- Compare interpolated fields with analytical values.
- Calculate and visualize interpolation error.

## Numerical Method
Linear interpolation is used to estimate the electric field at particle positions.

## Results
The project produces three plots:

1. Grid nodes and particle positions.
2. Grid electric field and interpolated particle electric fields.
3. Absolute interpolation error.

## Tools
- Python
- NumPy
- Matplotlib

## PIC Series

- Project 00 — Single Particle Motion
- Project 01 — 1D Charge Deposition Using Cloud-in-Cell (CIC)
- Project 02 — 1D Charge Density Calculation
- Project 03 — 1D Poisson Solver
- Project 04 — 1D Electric Field Calculation
- Project 05 — Grid-to-Particle Electric Field Interpolation

## Author
Laiba Iqbal
