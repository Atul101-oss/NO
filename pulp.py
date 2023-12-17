from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Create a linear programming problem
problem = LpProblem("Constrained_Optimization", LpMaximize)

# Define variables
x = LpVariable("x", lowBound=0)
y = LpVariable("y", lowBound=0)

# Define the objective function
objective_function = 3 * x + 2 * y
problem += objective_function, "Objective Function"

# Define constraints
constraint1 = 2 * x + y <= 20
constraint2 = 4 * x - 5 * y >= -10
constraint3 = x + 2 * y <= 10

problem += constraint1, "Constraint 1"
problem += constraint2, "Constraint 2"
problem += constraint3, "Constraint 3"

# Solve the problem
problem.solve()

# Display the results
print(f"Status: {problem.status}")
print(f"Optimal Solution:")
print(f"x = {x.varValue}")
print(f"y = {y.varValue}")
print(f"Optimal Objective Value: {objective_function.value()}")
