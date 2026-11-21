
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# PROJECT 03 — 1D POISSON SOLVER
# ============================================================

# 1. DEFINE THE COMPUTATIONAL GRID
x_min = 0.0
x_max = 10.0
N_grid = 101

dx = (x_max - x_min) / (N_grid - 1)
x_grid = np.linspace(x_min, x_max, N_grid)

# 2. DEFINE CHARGE DENSITY
rho = np.zeros(N_grid)

# Create a positive charge distribution near the center
rho[40:61] = 1.0e-9

# 3. DEFINE PHYSICAL CONSTANT
epsilon_0 = 8.8541878128e-12

# 4. DEFINE BOUNDARY CONDITIONS
phi_left = 0.0
phi_right = 0.0

# 5. SOLVE POISSON'S EQUATION USING FINITE DIFFERENCES
A = np.zeros((N_grid - 2, N_grid - 2))
b = np.zeros(N_grid - 2)

for i in range(N_grid - 2):
    A[i, i] = -2.0

    if i > 0:
        A[i, i - 1] = 1.0

    if i < N_grid - 3:
        A[i, i + 1] = 1.0

b = -(rho[1:-1] * dx**2) / epsilon_0

b[0] -= phi_left
b[-1] -= phi_right

phi_interior = np.linalg.solve(A, b)

# 6. CONSTRUCT THE FULL POTENTIAL ARRAY
phi = np.zeros(N_grid)

phi[0] = phi_left
phi[-1] = phi_right
phi[1:-1] = phi_interior

# 7. VERIFY THE SOLUTION
rho_reconstructed = np.zeros(N_grid)

rho_reconstructed[1:-1] = (
    -epsilon_0
    * (phi[2:] - 2.0 * phi[1:-1] + phi[:-2])
    / dx**2
)

print("Grid spacing:", dx)
print("Maximum potential:", np.max(phi), "V")
print("Minimum potential:", np.min(phi), "V")

print(
    "Poisson equation verification:",
    np.allclose(rho[1:-1], rho_reconstructed[1:-1])
)

# 8. VISUALIZE CHARGE DENSITY AND POTENTIAL
plt.figure(figsize=(8, 5))

plt.plot(x_grid, rho, color="blue")
plt.xlabel("Position (x)")
plt.ylabel("Charge Density (C/m³)")
plt.title("Charge Density on the 1D Grid")
plt.grid()

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

plt.plot(x_grid, phi, color="red")
plt.xlabel("Position (x)")
plt.ylabel("Electrostatic Potential (V)")
plt.title("1D Poisson Solver")
plt.grid()

plt.tight_layout()
plt.show()
