from vpython import sphere, rate, vector, color, curve
import numpy as np

# Constants
omega = 2.0
A = 1.0
alpha = np.sqrt(omega**2 - A**2)
beta = np.sqrt(omega**2 + A**2)

# Time setup
t_max = 20
dt = 0.01
t = 0

# Object and trail
ball = sphere(pos=vector(0, 0, 0), radius=0.2, color=color.red, make_trail=True)
trail = curve(color=color.yellow)

# Animation loop
while t < t_max:
    # Position based on general solution (sum of sines and cosines)
    x = np.cos(alpha * t) + 0.5 * np.sin(alpha * t) + 0.7 * np.cos(beta * t) + 0.3 * np.sin(beta * t)
    
    # We'll show motion along the x-axis (can expand to 3D if you want)
    ball.pos = vector(x, 0, 0)
    trail.append(pos=ball.pos)
    
    rate(100)  # Controls the speed of animation
    t += dt
