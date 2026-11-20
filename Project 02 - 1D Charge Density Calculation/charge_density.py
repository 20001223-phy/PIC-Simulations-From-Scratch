
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# PROJECT 02 — 1D CHARGE DENSITY CALCULATION
# ============================================================

# ------------------------------------------------------------
# 1. DEFINE THE COMPUTATIONAL GRID
# ------------------------------------------------------------

x_min = 0
x_max = 10
N_grid = 11

dx = (x_max - x_min) / (N_grid - 1)

x_grid = np.linspace(x_min, x_max, N_grid)


# ------------------------------------------------------------
# 2. DEFINE DEPOSITED GRID CHARGES
# ------------------------------------------------------------

grid_charge = np.array([
    0,
    0,
    -1.1214e-19,
    -4.8060e-20,
    0,
    -4.8060e-20,
    -1.1214e-19,
    0,
    -9.6120e-20,
    -6.4080e-20,
    0
])


# ------------------------------------------------------------
# 3. CALCULATE CHARGE DENSITY
# ------------------------------------------------------------

charge_density = grid_charge / dx


# ------------------------------------------------------------
# 4. DISPLAY CHARGE DENSITY
# ------------------------------------------------------------

print("Grid positions:", x_grid)
print("Grid spacing:", dx)
print("Grid charge:", grid_charge)
print("Charge density:", charge_density)


# ------------------------------------------------------------
# 5. CHECK TOTAL CHARGE
# ------------------------------------------------------------

total_grid_charge = np.sum(grid_charge)

total_charge_from_density = np.sum(charge_density * dx)

print("Total grid charge:", total_grid_charge)
print("Total charge from density:", total_charge_from_density)

print(
    "Charge conservation:",
    np.isclose(total_grid_charge, total_charge_from_density)
)


# ------------------------------------------------------------
# 6. VISUALIZE CHARGE DENSITY
# ------------------------------------------------------------

plt.figure()

plt.bar(
    x_grid,
    charge_density,
    width=0.7,
    color='blue',
    edgecolor='black'
)

plt.xlabel("Position (x)")
plt.ylabel("Charge Density (C/m^3)")
plt.title("One-Dimensional Charge Density")

plt.grid(axis='y')

plt.show()
