import matplotlib.pyplot as plt
import numpy as np

# Define the function
def f(x):
    return x**2 - 4*x + 3

# Generate x values
x = np.linspace(-2, 6, 400)
y = f(x)

# Find the vertex (minimum point)
x_min = 2
y_min = f(x_min)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='f(x) = x² - 4x + 3', color='blue')
plt.plot(x_min, y_min, 'ro', label='Minimum Point (2, -1)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Annotate the minimum point
plt.annotate('Minimum',
             xy=(x_min, y_min),
             xytext=(x_min + 0.5, y_min + 5),
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=12)

plt.title('Graph of f(x) = x² - 4x + 3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
