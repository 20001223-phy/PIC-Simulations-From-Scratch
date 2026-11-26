# PIC Simulations From Scratch

A collection of computational physics projects developed from scratch using Python, with a focus on Particle-in-Cell (PIC) simulations and plasma physics.

This repository documents a step-by-step exploration of numerical methods used in computational plasma physics, beginning with single-particle dynamics and progressing toward grid-based field calculations and particle-grid interactions, with the eventual goal of implementing self-consistent PIC simulations.

## Projects

### Project 00 — Single Particle Motion
Numerical simulation of a charged particle moving under a uniform electric field, using Euler and trapezoidal integration methods. Includes comparisons with the analytical solution and numerical error analysis.

### Project 01 — 1D Charge Deposition Using Cloud-in-Cell (CIC)
Implementation of the Cloud-in-Cell method to distribute particle charges onto a one-dimensional computational grid using weighted charge deposition.

### Project 02 — 1D Charge Density Calculation
Calculation and visualization of charge density from deposited grid charges, including a charge conservation check.

### Project 03 — 1D Poisson Solver
Numerical solution of the one-dimensional Poisson equation using the finite difference method to calculate electrostatic potential from a prescribed charge-density distribution. Includes numerical verification and visualizations of charge density and potential.

### Project 04 — 1D Electric Field Calculation
Numerical calculation of the one-dimensional electric field from a prescribed Gaussian electrostatic potential using finite difference methods. Includes comparison with the analytical electric field and numerical error analysis.

### Project 05 — Grid-to-Particle Electric Field Interpolation
Implementation of linear interpolation to estimate the electric field at particle positions from electric field values defined on grid nodes. Includes comparison with the analytical electric field and interpolation error analysis.

## Tools and Technologies

- Python
- NumPy
- Matplotlib
- Visual Studio Code
- Git and GitHub

## Learning Approach

Each project focuses on an individual computational concept and is developed as an independent, executable Python program.

Projects include source code, documentation, and visualizations where applicable. Numerical results are compared with analytical solutions whenever possible to evaluate the accuracy of the implemented methods.

## Future Work

The repository will progressively explore:

- Particle initialization and numerical particle pushing
- Integration of charge deposition, field solving, interpolation, and particle motion
- Self-consistent one-dimensional electrostatic PIC simulations
- Plasma instabilities and wave phenomena
- Extensions toward two-dimensional and electromagnetic PIC simulations
