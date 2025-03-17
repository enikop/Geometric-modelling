import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Define the parametric equations
u = np.linspace(-5, 5, 50)
v = np.linspace(-5, 5, 50)
u, v = np.meshgrid(u, v)

# Example: Parametric equations for a sphere
x = u
y = v
z = u**3 +(u-2)**2+(v+1)**3-(v+2)**2
# Create the 3D figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, facecolors=cm.viridis((z + 15) / 30), alpha=1.0)

# Select a specific parameter value
u0 = 1
v0 = 2
x0 = u0
y0 = v0
z0 = u0**3 +(u0-2)**2+(v0+1)**3-(v0+2)**2
ax.scatter(x0, y0, z0, color='red', s=100, label='Selected Point')

# Compute normal vector
zx_u = 3 * u0**2 + 2 * (u0 - 2)
zx_v = 3 * (v0 + 1)**2 - 2 * (v0 + 2)
nx, ny, nz = -zx_u, -zx_v, 1
norm_length = 0.5
ax.quiver(x0, y0, z0, nx, ny, nz, color='blue', length=norm_length, linewidth=2, label='Normal Vector')


# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_zlim(-15,15)
ax.set_aspect('equal')
ax.set_title('3D Parametric Surface with Features')
ax.legend()

plt.show()
