
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# PROJECT 04 — 1D ELECTRIC FIELD CALCULATION
# ============================================================

# 1. DEFINE THE COMPUTATIONAL GRID

x_min = 0.0
x_max = 10.0
N_grid = 101

dx = (x_max - x_min) / (N_grid - 1)

x_grid = np.linspace(x_min, x_max, N_grid)


# 2. DEFINE THE ELECTROSTATIC POTENTIAL

phi_0 = 10.0
x_0 = 5.0
sigma = 1.0

phi = phi_0 * np.exp(-((x_grid - x_0) / sigma)**2)


# 3. CALCULATE THE ELECTRIC FIELD NUMERICALLY

E = np.zeros(N_grid)

# Central difference method for interior points

E[1:-1] = -(
    phi[2:] - phi[:-2]
) / (2.0 * dx)

# Forward difference at the left boundary

E[0] = -(phi[1] - phi[0]) / dx

# Backward difference at the right boundary

E[-1] = -(phi[-1] - phi[-2]) / dx


# 4. CALCULATE THE ANALYTICAL ELECTRIC FIELD

E_analytical = (
    (2.0 * phi_0 * (x_grid - x_0)) / sigma**2
    * np.exp(-((x_grid - x_0) / sigma)**2)
)


# 5. CALCULATE THE NUMERICAL ERROR

error = np.abs(E - E_analytical)

max_error = np.max(error)


# 6. DISPLAY RESULTS

print("Grid spacing:", dx)

print(
    "Maximum numerical electric field:",
    np.max(np.abs(E)),
    "V/m"
)

print(
    "Maximum analytical electric field:",
    np.max(np.abs(E_analytical)),
    "V/m"
)

print(
    "Maximum absolute error:",
    max_error,
    "V/m"
)


# 7. VISUALIZE ELECTROSTATIC POTENTIAL

plt.figure(figsize=(8, 5))

plt.plot(x_grid, phi, label="Electrostatic Potential")

plt.xlabel("Position (m)")
plt.ylabel("Potential (V)")
plt.title("1D Electrostatic Potential Distribution")

plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("potential_distribution.png", dpi=300)
plt.show()


# 8. VISUALIZE ELECTRIC FIELD

plt.figure(figsize=(8, 5))

plt.plot(
    x_grid,
    E,
    label="Numerical Electric Field"
)

plt.plot(
    x_grid,
    E_analytical,
    "--",
    label="Analytical Electric Field"
)

plt.xlabel("Position (m)")
plt.ylabel("Electric Field (V/m)")
plt.title("1D Electric Field Distribution")

plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("electric_field_comparison.png", dpi=300)
plt.show()


# 9. VISUALIZE NUMERICAL ERROR

plt.figure(figsize=(8, 5))

plt.plot(x_grid, error)

plt.xlabel("Position (m)")
plt.ylabel("Absolute Error (V/m)")
plt.title("Numerical Error in Electric Field Calculation")

plt.grid()
plt.tight_layout()
plt.savefig("electric_field_error.png", dpi=300)
plt.show()
