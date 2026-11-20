
# ============================================================
# Project 00: Single Particle Motion
# Electron in a Uniform Electric Field
# ============================================================
#
# Description:
# Simulate the motion of an electron in a constant, uniform
# electric field using analytical equations and two numerical
# integration methods: Forward Euler and Trapezoidal.
#
# ============================================================


# 1. IMPORT LIBRARIES

import matplotlib.pyplot as plt
import numpy as np


# 2. PHYSICAL PARAMETERS AND ELECTRIC FORCE

# Electron properties and electric field
q = -1.602e-19       # Electron charge (C)
m = 9.109e-31        # Electron mass (kg)
E = 1.0              # Electric field (V/m)

# Calculate electric force and acceleration
F = q * E
a = F / m

print("Electric force:", F, "N")
print("Electron acceleration:", a, "m/s^2")


# 3. ANALYTICAL SOLUTION: VELOCITY AND POSITION

# Initial conditions
x_0 = 0.0            # Initial position (m)
v_0 = 0.0            # Initial velocity (m/s)

# Total simulation time: 1 nanosecond
t = 1e-9

# Analytical velocity and position at final time
v = v_0 + a * t
x = x_0 + v_0 * t + 0.5 * a * t**2

print("Electron velocity:", v, "m/s")
print("Electron position:", x, "m")


# 4. ANALYTICAL MOTION PLOTS

# Plot 1: Electron position at 1 ns

plt.figure(figsize=(8, 5))
plt.scatter(t, x)

plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Electron Position at 1 ns")
plt.grid()
plt.show()


# Generate 100 equally spaced time points
time = np.linspace(0, 1e-9, 100)

# Calculate analytical position and velocity
position = x_0 + v_0 * time + 0.5 * a * time**2
velocity = v_0 + a * time


# Plot 2: Analytical position versus time

plt.figure(figsize=(8, 5))
plt.plot(time, position, label="Analytical solution")

plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Electron Motion in a Uniform Electric Field")
plt.legend()
plt.grid()
plt.show()


# Plot 3: Analytical velocity versus time

plt.figure(figsize=(8, 5))
plt.plot(time, velocity)

plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Electron Velocity vs. Time")
plt.grid()
plt.show()


# 5. NUMERICAL SIMULATION SETUP

# Number of simulation steps
N_steps = 1000

# Calculate time step
dt = 1e-9 / N_steps

print("Time step (dt):", dt, "s")

# Create arrays to store numerical results
# 1000 updates require 1001 entries, including the initial condition.

x_numerical = np.zeros(N_steps + 1)
v_numerical = np.zeros(N_steps + 1)

x_trapezoidal = np.zeros(N_steps + 1)
v_trapezoidal = np.zeros(N_steps + 1)

# Set initial conditions
x_numerical[0] = x_0
v_numerical[0] = v_0

x_trapezoidal[0] = x_0
v_trapezoidal[0] = v_0

print("Initial position:", x_numerical[0], "m")
print("Initial velocity:", v_numerical[0], "m/s")


# 6. FORWARD EULER METHOD

# Forward Euler updates velocity and position step by step.
# Position is updated using the velocity at the beginning
# of each time step.

for n in range(N_steps):

    v_numerical[n + 1] = v_numerical[n] + a * dt

    x_numerical[n + 1] = (
        x_numerical[n] + v_numerical[n] * dt
    )


print("Euler final velocity:", v_numerical[-1])
print("Euler final position:", x_numerical[-1])


# 7. TRAPEZOIDAL METHOD

# Trapezoidal method updates position using the average
# of the velocities at the beginning and end of each step.

for n in range(N_steps):

    v_trapezoidal[n + 1] = v_trapezoidal[n] + a * dt

    x_trapezoidal[n + 1] = (
        x_trapezoidal[n]
        + (v_trapezoidal[n] + v_trapezoidal[n + 1]) / 2 * dt
    )


print("Trapezoidal final velocity:", v_trapezoidal[-1])
print("Trapezoidal final position:", x_trapezoidal[-1])


# 8. ANALYTICAL VS NUMERICAL COMPARISON

# Calculate final velocity and position errors
# by comparing numerical results with analytical results.

print("Euler velocity error:", abs(v_numerical[-1] - v))
print("Euler position error:", abs(x_numerical[-1] - x))

print("Trapezoidal velocity error:", abs(v_trapezoidal[-1] - v))
print("Trapezoidal position error:", abs(x_trapezoidal[-1] - x))


# Generate time array for numerical results
time_numerical = np.linspace(0, 1e-9, N_steps + 1)


# Plot 4: Analytical versus numerical position

plt.figure(figsize=(8, 5))

plt.plot(time, position, label="Analytical solution")

plt.plot(
    time_numerical,
    x_numerical,
    "--",
    label="Euler numerical solution"
)

plt.plot(
    time_numerical,
    x_trapezoidal,
    label="Trapezoidal numerical solution"
)

plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Analytical vs Numerical Electron Motion")
plt.legend()
plt.grid()
plt.show()


# 9. POSITION ERROR ANALYSIS

# Calculate analytical position at every numerical time step

analytical_position = (
    x_0 + v_0 * time_numerical
    + 0.5 * a * time_numerical**2
)

# Calculate absolute position errors

position_error_euler = np.abs(
    x_numerical - analytical_position
)

position_error_trapezoidal = np.abs(
    x_trapezoidal - analytical_position
)

# Print final position errors

print(
    "Euler error at final time:",
    position_error_euler[-1],
    "m"
)

print(
    "Trapezoidal error at final time:",
    position_error_trapezoidal[-1],
    "m"
)

print(
    "Number of Euler error values:",
    len(position_error_euler)
)

print(
    "Number of Trapezoidal error values:",
    len(position_error_trapezoidal)
)


# 10. POSITION ERROR PLOT

# Plot 5: Absolute position error versus time

plt.figure(figsize=(8, 5))

plt.plot(
    time_numerical,
    position_error_euler,
    label="Euler position error"
)

plt.plot(
    time_numerical,
    position_error_trapezoidal,
    label="Trapezoidal position error"
)

plt.xlabel("Time (s)")
plt.ylabel("Absolute Position Error (m)")
plt.title("Position Error vs. Time")
plt.legend()
plt.grid()
plt.show()
