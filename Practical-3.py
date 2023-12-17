import numpy as np
import matplotlib.pyplot as plt

# Decision variables
x = np.linspace(0, 20, 100)

# Constraints
eq1 = (2 * x - 20)  # 2x - y <= 20
eq2 = (50 - 4 * x) / 5  # 4x + 5y <= 50
eq3 = np.zeros_like(x)  # x >= 0
eq4 = (3 * x) / 2  # 3x - 2y >= 0

# Feasible region
plt.plot(x, eq1, label=r'$2x - y \leq 20$')
plt.plot(x, eq2, label=r'$4x + 5y \leq 50$')
plt.plot(x, eq4, label=r'$3x - 2y \geq 0$')
plt.fill_between(x, 0, np.minimum.reduce([eq1, eq2, eq3, eq4]), color='gray', alpha=0.5, label='Feasible Region')

# Axis labels
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# Add labels and legend
plt.title('Feasible Region')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Identify corner points
corner_points_x = [0, 0, 10, 15]
corner_points_y = [0, 20, 5, 0]

# Plot corner points
plt.scatter(corner_points_x, corner_points_y, color='red', label='Corner Points')

# Add labels for corner points
for i, txt in enumerate(corner_points_x):
    plt.annotate(f'({corner_points_x[i]}, {corner_points_y[i]})', (corner_points_x[i], corner_points_y[i]))

# Show the plot
plt.show()

# Evaluate the objective function at each corner point
objective_function_values = [3 * x + 4 * y for x, y in zip(corner_points_x, corner_points_y)]

# Identify the optimal solution
optimal_point_index = np.argmax(objective_function_values)
optimal_point = (corner_points_x[optimal_point_index], corner_points_y[optimal_point_index])
optimal_value = objective_function_values[optimal_point_index]

print("Optimal Solution:")
print(f"x = {optimal_point[0]}, y = {optimal_point[1]}")
print(f"Optimal Objective Value: {optimal_value}")
