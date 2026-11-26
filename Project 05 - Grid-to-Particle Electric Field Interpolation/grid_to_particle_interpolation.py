
import numpy as np
import matplotlib.pyplot as plt

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

# 3. CALCULATE THE ELECTRIC FIELD ON THE GRID
E_grid = np.zeros(N_grid)

E_grid[1:-1] = -(phi[2:] - phi[:-2]) / (2.0 * dx)
E_grid[0] = -(phi[1] - phi[0]) / dx
E_grid[-1] = -(phi[-1] - phi[-2]) / dx

# 4. DEFINE PARTICLE POSITIONS
x_particles = np.array([1.35, 2.75, 4.2, 5.6, 7.15, 8.65])

# 5. INTERPOLATE ELECTRIC FIELD TO PARTICLE POSITIONS
E_particles = np.interp(x_particles, x_grid, E_grid)

# 6. CALCULATE ANALYTICAL ELECTRIC FIELD
E_analytical_particles = (
    (2.0 * phi_0 * (x_particles - x_0)) / sigma**2
    * np.exp(-((x_particles - x_0) / sigma)**2)
)

# 7. CALCULATE INTERPOLATION ERROR
error = np.abs(E_particles - E_analytical_particles)
max_error = np.max(error)

# 8. DISPLAY RESULTS
print("Grid spacing:", dx)
print()

print("Particle positions and interpolated electric fields:")
for i in range(len(x_particles)):
    print(
        f"Particle {i}: x = {x_particles[i]:.2f} m, "
        f"E = {E_particles[i]:.6f} V/m, "
        f"Analytical E = {E_analytical_particles[i]:.6f} V/m, "
        f"Error = {error[i]:.6e} V/m"
    )

print()
print("Maximum interpolation error:", max_error, "V/m")

# 9. VISUALIZE GRID AND PARTICLE POSITIONS
plt.figure(figsize=(8, 5))

plt.plot(x_grid, E_grid, label="Electric Field on Grid")
plt.scatter(
    x_particles,
    np.zeros_like(x_particles),
    label="Particle Positions",
    marker="x"
)

plt.xlabel("Position (m)")
plt.ylabel("Electric Field (V/m)")
plt.title("Grid Nodes and Particle Positions")
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("figures/grid_and_particles.png", dpi=300)
plt.show()

# 10. VISUALIZE INTERPOLATED ELECTRIC FIELD
plt.figure(figsize=(8, 5))

plt.plot(x_grid, E_grid, label="Grid Electric Field")
plt.scatter(
    x_particles,
    E_particles,
    label="Interpolated Field at Particles",
    marker="o"
)

plt.xlabel("Position (m)")
plt.ylabel("Electric Field (V/m)")
plt.title("Grid-to-Particle Electric Field Interpolation")
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("figures/field_interpolation.png", dpi=300)
plt.show()

# 11. VISUALIZE INTERPOLATION ERROR
plt.figure(figsize=(8, 5))

plt.plot(x_particles, error, marker="o")

plt.xlabel("Particle Position (m)")
plt.ylabel("Absolute Error (V/m)")
plt.title("Interpolation Error at Particle Positions")
plt.grid()
plt.tight_layout()
plt.savefig("figures/interpolation_error.png", dpi=300)
plt.show()
