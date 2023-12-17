from scipy.optimize import minimize

# Define the objective function
def objective_function(x):
    return x[0]**2 + 4 * x[1]**2 - 2 * x[0] * x[1] - 4 * x[0]

# Define the constraints
constraints = (
    {'type': 'ineq', 'fun': lambda x: x[0] + x[1] - 3},
    {'type': 'ineq', 'fun': lambda x: -x[0] - x[1] + 0.5}
)

# Define the initial guess
initial_guess = [0, 0]

# Solve the constrained optimization problem
result = minimize(objective_function, initial_guess, constraints=constraints)

# Display the results
print("Optimal Solution:")
print(f"x: {result.x[0]}")
print(f"y: {result.x[1]}")
print(f"Optimal Value: {result.fun}")
