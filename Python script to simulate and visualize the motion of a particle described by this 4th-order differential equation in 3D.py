import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
omega = 2.0
A = 1.0
alpha = np.sqrt(omega**2 - A**2)
beta = np.sqrt(omega**2 + A**2)

# Time array
t = np.linspace(0, 20, 1000)

# General solution using sine and cosine components
x = np.cos(alpha * t) + 0.5 * np.sin(alpha * t) + 0.7 * np.cos(beta * t) + 0.3 * np.sin(beta * t)
v = np.gradient(x, t)           # First derivative (velocity)
a = np.gradient(v, t)           # Second derivative (acceleration)

# Plotting in 3D: position vs velocity vs acceleration
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, v, a, color='blue')

# Labels and title
ax.set_title("3D Motion: x(t), v(t), a(t)")
ax.set_xlabel("Position x(t)")
ax.set_ylabel("Velocity x'(t)")
ax.set_zlabel("Acceleration x''(t)")

plt.tight_layout()
plt.show()
