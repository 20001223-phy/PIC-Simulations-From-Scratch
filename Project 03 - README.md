
# Project 03 — 1D Poisson Solver

## Overview

This project implements a one-dimensional numerical solver for Poisson's equation using the finite difference method in Python.

The solver calculates the electrostatic potential from a specified charge-density distribution on a computational grid. The resulting potential is verified by reconstructing the charge density using the discrete Poisson equation.

This project is part of my **PIC Simulations from Scratch** series, where I progressively implement the fundamental numerical methods used in Particle-in-Cell simulations.

## Physics

In one dimension, Poisson's equation is given by:

\[
\frac{d^2\phi}{dx^2}=-\frac{\rho}{\varepsilon_0}
\]

where:

- $\phi$ is the electrostatic potential (V)
- $\rho$ is the charge density (C/m³)
- $\varepsilon_0$ is the vacuum permittivity (F/m)

The electrostatic potential is calculated from a prescribed charge-density distribution using fixed boundary conditions:

\[
\phi(0)=0,\qquad \phi(10)=0
\]

## Numerical Method

The second spatial derivative of the potential is approximated using the central finite difference method:

\[
\frac{d^2\phi}{dx^2}
\approx
\frac{\phi_{i+1}-2\phi_i+\phi_{i-1}}{\\Delta x^2}
\]

Substituting this approximation into Poisson's equation gives:

\[
\phi_{i+1}-2\phi_i+\phi_{i-1}
=
-\frac{\rho_i\Delta x^2}{\varepsilon_0}
\]

This equation is applied at each interior grid point, producing a system of linear equations:

\[
A\boldsymbol{\phi}=\mathbf{b}
\]

The linear system is solved using NumPy's `np.linalg.solve()`.

## Model Setup

- Spatial domain: $0 \leq x \leq 10$
- Number of grid points: 101
- Grid spacing: $\Delta x = 0.1$
- Boundary potentials: $\phi(0)=\phi(10)=0$
- Charge density: Uniform positive charge in the central region of the domain
- Numerical method: Central finite difference
- Linear solver: NumPy

## Verification

The calculated potential is substituted back into the discrete Poisson equation to reconstruct the charge density.

The reconstructed charge density is compared with the original prescribed charge density using `np.allclose()`.

This checks whether the numerical solution satisfies the discrete Poisson equation within floating-point tolerance.

## Results

The project generates two plots:

1. **Charge Density Distribution** — Shows the prescribed charge density across the computational grid.
2. **Electrostatic Potential** — Shows the potential calculated from the charge-density distribution.

## Tools Used

- Python
- NumPy
- Matplotlib

## How to Run

```bash
python poisson_solver.py
```

## PIC Simulations from Scratch

| Project | Description |
|---|---|
| Project 00 | Single Particle Motion |
| Project 01 | 1D Charge Deposition Using CIC |
| Project 02 | 1D Charge Density Calculation |
| Project 03 | 1D Poisson Solver |

## Next Project

**Project 04 — 1D Electric Field Calculation**

The next project will calculate the electric field from the electrostatic potential using:

\[
E_x=-\frac{d\phi}{dx}
\]

## Author

Laiba Iqbal
