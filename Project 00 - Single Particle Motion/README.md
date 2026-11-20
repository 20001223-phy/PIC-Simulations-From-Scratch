# Project 00 — Single Particle Motion

## Overview

This project simulates the motion of a single electron in a constant, uniform electric field using Python.

It introduces the numerical integration of particle equations of motion and compares two numerical methods:

- Forward Euler Method
- Trapezoidal Method

The project is a foundational exercise for learning computational plasma physics and preparing for Particle-in-Cell (PIC) simulations.

## Physical Model

An electron is initially at rest in a uniform electric field.

The electric force acting on the electron is:

\[
F=qE
\]

The resulting acceleration is:

\[
a=\frac{qE}{m}
\]

The equations of motion are:

\[
\frac{dv}{dt}=a
\]

\[
\frac{dx}{dt}=v
\]

## Simulation Parameters

| Parameter | Value |
|---|---:|
| Particle | Electron |
| Charge | \(-1.602\times10^{-19}\) C |
| Mass | \(9.109\times10^{-31}\) kg |
| Electric field | \(1\) V/m |
| Initial position | \(0\) m |
| Initial velocity | \(0\) m/s |
| Total simulation time | \(1\times10^{-9}\) s |
| Number of time steps | 1000 |
| Time step | \(1\times10^{-12}\) s |

## Numerical Methods

### 1. Forward Euler Method

Velocity update:

\[
v_{n+1}=v_n+a\Delta t
\]

Position update:

\[
x_{n+1}=x_n+v_n\Delta t
\]

### 2. Trapezoidal Method

Velocity update:

\[
v_{n+1}=v_n+a\Delta t
\]

Position update:

\[
x_{n+1}=x_n+\frac{v_n+v_{n+1}}{2}\Delta t
\]

## Results

The numerical results are compared with the analytical solution.

| Quantity | Analytical value |
|---|---:|
| Final velocity | \(-175.8700\) m/s |
| Final position | \(-8.7935\times10^{-8}\) m |

For this constant-acceleration problem, the trapezoidal method gives a much smaller position error than the Forward Euler method.

## Visualizations

The Python script generates five plots:

1. Electron position at the final simulation time.
2. Analytical position versus time.
3. Analytical velocity versus time.
4. Analytical and numerical position comparison.
5. Absolute position error versus time.

## Requirements

- Python 3
- NumPy
- Matplotlib

Install the required libraries:

```bash
pip install numpy matplotlib
```

## How to Run

Clone this repository or download the project file.

Run:

```bash
python single_particle.py
```

## Learning Objectives

- Understand charged-particle motion in an electric field.
- Calculate electric force and particle acceleration.
- Implement numerical integration in Python.
- Compare numerical solutions with analytical solutions.
- Understand numerical errors and time-step dependence.

## Next Steps

This project is the starting point for a series of computational plasma physics projects, gradually progressing toward one-dimensional electrostatic Particle-in-Cell (PIC) simulations.

---

**Project 00 — Single Particle Motion**  
*Computational Plasma Physics | Python*
