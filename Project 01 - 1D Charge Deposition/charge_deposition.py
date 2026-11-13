import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# PROJECT 01 — 1D CHARGE DEPOSITION USING CLOUD-IN-CELL (CIC)
# ============================================================

# ------------------------------------------------------------
# 1. DEFINE THE COMPUTATIONAL DOMAIN
# ------------------------------------------------------------

x_min = 0
x_max = 10
N_grid = 11

dx = (x_max - x_min) / (N_grid - 1)

x_grid = np.linspace(x_min, x_max, N_grid)

print("Grid points:", x_grid)
print("Grid spacing:", dx)
print("Number of grid points:", len(x_grid))


# ------------------------------------------------------------
# 2. VISUALIZE THE COMPUTATIONAL GRID
# ------------------------------------------------------------

plt.figure()

plt.scatter(
    x_grid,
    np.zeros(N_grid),
    color='blue',
    label='Grid points'
)

plt.xlabel("Position (x)")
plt.ylabel("Grid")
plt.title("One-Dimensional Computational Grid")
plt.legend()
plt.grid()

plt.show()


# ------------------------------------------------------------
# 3. DEFINE PARTICLE POSITIONS
# ------------------------------------------------------------

particle_positions = np.array([2.3, 5.7, 8.4])

print("Particle positions:", particle_positions)


# ------------------------------------------------------------
# 4. VISUALIZE PARTICLES AND GRID
# ------------------------------------------------------------

plt.figure()

plt.scatter(
    x_grid,
    np.zeros(N_grid),
    color='blue',
    label='Grid points'
)

plt.scatter(
    particle_positions,
    np.zeros(len(particle_positions)),
    color='red',
    marker='x',
    s=100,
    label='Particles'
)

plt.xlabel("Position (x)")
plt.ylabel("Grid")
plt.title("Particles and Computational Grid")
plt.legend()
plt.grid()

plt.show()


# ------------------------------------------------------------
# 5. IDENTIFY THE LEFT AND RIGHT GRID NEIGHBORS
# ------------------------------------------------------------

left_indices = np.floor(
    (particle_positions - x_min) / dx
).astype(int)

right_indices = left_indices + 1

print("Left grid indices:", left_indices)
print("Right grid indices:", right_indices)


# ------------------------------------------------------------
# 6. CALCULATE CIC WEIGHTS
# ------------------------------------------------------------

left_grid_positions = x_grid[left_indices]
right_grid_positions = x_grid[right_indices]

left_weights = (
    right_grid_positions - particle_positions
) / dx

right_weights = (
    particle_positions - left_grid_positions
) / dx

print("Left weights:", left_weights)
print("Right weights:", right_weights)

print("Sum of weights:", left_weights + right_weights)


# ------------------------------------------------------------
# 7. DEFINE PARTICLE CHARGES
# ------------------------------------------------------------

q_e = -1.602e-19

particle_charges = np.array([
    q_e,
    q_e,
    q_e
])

print("Particle charges:", particle_charges)


# ------------------------------------------------------------
# 8. CALCULATE CHARGE CONTRIBUTIONS
# ------------------------------------------------------------

left_charge = particle_charges * left_weights

right_charge = particle_charges * right_weights

print("Left charge contributions:", left_charge)
print("Right charge contributions:", right_charge)


# ------------------------------------------------------------
# 9. INITIALIZE GRID CHARGE ARRAY
# ------------------------------------------------------------

grid_charge = np.zeros(N_grid)

print("Initial grid charge:", grid_charge)


# ------------------------------------------------------------
# 10. DEPOSIT PARTICLE CHARGES ONTO THE GRID
# ------------------------------------------------------------

np.add.at(
    grid_charge,
    left_indices,
    left_charge
)

np.add.at(
    grid_charge,
    right_indices,
    right_charge
)

print("Deposited charge on grid:", grid_charge)


# ------------------------------------------------------------
# 11. CHECK CHARGE CONSERVATION
# ------------------------------------------------------------

total_particle_charge = np.sum(particle_charges)

total_grid_charge = np.sum(grid_charge)

print("Total particle charge:", total_particle_charge)

print("Total deposited grid charge:", total_grid_charge)

print(
    "Charge conservation:",
    np.isclose(total_particle_charge, total_grid_charge)
)


# ------------------------------------------------------------
# 12. VISUALIZE DEPOSITED CHARGE
# ------------------------------------------------------------

plt.figure()

plt.bar(
    x_grid,
    grid_charge,
    width=0.7,
    color='blue',
    edgecolor='black'
)

plt.xlabel("Position (x)")
plt.ylabel("Deposited Charge (C)")
plt.title("Cloud-in-Cell Charge Deposition")

plt.grid(axis='y')

plt.show()
