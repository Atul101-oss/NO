import numpy as np
from scipy.optimize import minimize_scalar

# Define the objective function
def objective_function(x):
    return (x - 2)**2 + 3 * np.sin(5 * x)

# Golden Section Rule for Line Search
def golden_section_line_search(func, a, b, tol=1e-6):
    golden_ratio = (1 + np.sqrt(5)) / 2

    # Initial interval [a, b]
    interval_length = b - a

    # Set initial points
    x1 = b - (1 / golden_ratio) * interval_length
    x2 = a + (1 / golden_ratio) * interval_length

    while interval_length > tol:
        if func(x1) < func(x2):
            b = x2
            x2 = x1
            x1 = b - (1 / golden_ratio) * (b - a)
        else:
            a = x1
            x1 = x2
            x2 = a + (1 / golden_ratio) * (b - a)

        interval_length = b - a

    return (a + b) / 2

# Fibonacci Sequence for Line Search
def fibonacci_line_search(func, a, b, n, tol=1e-6):
    # Generate Fibonacci sequence
    fib_sequence = [1, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    fib_sequence.pop()

    # Initial interval [a, b]
    interval_length = b - a

    for k in range(len(fib_sequence) - 2, -1, -1):
        x1 = a + (fib_sequence[k] / fib_sequence[k + 2]) * interval_length
        x2 = a + (fib_sequence[k + 1] / fib_sequence[k + 2]) * interval_length

        if func(x1) < func(x2):
            b = x2
        else:
            a = x1

    return (a + b) / 2

if __name__ == "__main__":
    # Set the initial interval [a, b]
    a, b = -5, 5

    # Golden Section Rule Line Search
    golden_section_result = golden_section_line_search(objective_function, a, b)
    print(f"Golden Section Rule Optimal Solution: x = {golden_section_result}")
    print(f"Objective Value: {objective_function(golden_section_result)}\n")

    # Fibonacci Sequence Line Search
    n = 21  # Choose the number of Fibonacci sequence terms
    fibonacci_result = fibonacci_line_search(objective_function, a, b, n)
    print(f"Fibonacci Sequence Optimal Solution: x = {fibonacci_result}")
    print(f"Objective Value: {objective_function(fibonacci_result)}")
