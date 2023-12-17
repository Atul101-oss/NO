import numpy as np
import matplotlib.pyplot as plt

# Define the objective function
def objective_function(x):
    return -10 * np.cos(np.pi * x - 2.2) + (x + 1.5) * x

# Generate x values
x_values = np.linspace(-5, 5, 1000)

# Compute y values (function values)
y_values = objective_function(x_values)

# Plot the function
plt.plot(x_values, y_values, label='f(x)')

# Mark the minimum/maximum point
optimal_x = x_values[np.argmin(y_values)]
optimal_y = np.min(y_values)
plt.scatter(optimal_x, optimal_y, color='red', label='Global Optimal Solution')

# Add labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of the Function')

# Add legend
plt.legend()

# Show the plot
plt.show()

print(f"Global Optimal Solution: x = {optimal_x}, f(x) = {optimal_y}")
