
# Project 04 — 1D Electric Field Calculation

## Overview

This project implements a numerical calculation of the one-dimensional electric field from a prescribed electrostatic potential using the finite-difference method.

The electric field is obtained from the negative spatial derivative of the electrostatic potential:

\[
E(x) = -\frac{d\phi}{dx}
\]

A Gaussian potential distribution is used to calculate the electric field numerically. The numerical results are then compared with the analytical electric field to evaluate the accuracy of the finite-difference approximation.

## Objectives

- Define a one-dimensional computational grid.
- Generate a prescribed Gaussian electrostatic potential.
- Calculate the electric field using finite-difference methods.
- Implement central, forward, and backward difference schemes.
- Derive the analytical electric field for comparison.
- Calculate the absolute numerical error.
- Visualize the potential, electric field, and numerical error.

## Numerical Methods

### 1. Electrostatic Potential

The Gaussian potential distribution is defined as:

\[
\phi(x) = \phi_0 e^{-(x-x_0)^2/\sigma^2}
\]

### 2. Numerical Electric Field

The electric field is calculated using:

\[
E(x) = -\frac{d\phi}{dx}
\]

For interior grid points, the central difference approximation is used:

\[
E_i \approx -\frac{\phi_{i+1}-\phi_{i-1}}{2\Delta x}
\]

At the boundaries, forward and backward difference approximations are applied.

### 3. Analytical Electric Field

The analytical electric field corresponding to the Gaussian potential is:

\[
E(x) =
\frac{2\phi_0(x-x_0)}{\sigma^2}
e^{-(x-x_0)^2/\sigma^2}
\]

### 4. Numerical Error

The absolute error is calculated as:

\[
\text{Error} = |E_{\text{numerical}}-E_{\text{analytical}}|
\]

## Parameters

| Parameter | Value |
|---|---:|
| Minimum position | 0 m |
| Maximum position | 10 m |
| Number of grid points | 101 |
| Grid spacing | 0.1 m |
| Potential amplitude | 10 V |
| Gaussian centre | 5 m |
| Gaussian width | 1 m |

## Tools and Technologies

- Python
- NumPy
- Matplotlib
- Visual Studio Code

## Results and Visualizations

The project generates three figures:

1. **Potential Distribution:** Gaussian electrostatic potential across the computational domain.
2. **Electric Field Comparison:** Numerical electric field compared with its analytical solution.
3. **Numerical Error:** Absolute difference between numerical and analytical electric-field values.

## How to Run

Install the required libraries:

```bash
pip install numpy matplotlib
```

Run the Python script:

```bash
python electric_field.py
```

## Learning Outcomes

This project demonstrates how the electrostatic field can be calculated from the spatial derivative of electric potential using numerical differentiation.

It also introduces numerical accuracy assessment through comparison with an analytical solution.

## Future Work

- Interpolation of electric fields to particle positions.
- Particle initialization and numerical particle pushing.
- Development of a self-consistent one-dimensional electrostatic PIC simulation.
