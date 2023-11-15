# Import PuLP library
from pulp import *

# max problem:
problem = LpProblem("Knapsack_Problem", LpMaximize)

# variables (name, low bound, up bound, category):
x1 = LpVariable("item_0", 0, None, LpInteger)
x2 = LpVariable("item_1", 0, None, LpInteger)
x3 = LpVariable("item_2", 0, None, LpInteger)

# utility function:
problem += 11 * x1 + 7 * x2 + 12 * x3

# constraint:
problem += 4 * x1 + 3 * x2 + 5 * x3 <= 10

# The problem is solved using PuLP's choice of Solver
problem.solve()

# The status of the solution is printed to the screen
print(f"Status: {LpStatus[problem.status]}\n")

# Each of the variables is printed with it's resolved optimum value
for v in problem.variables():
    print(f"{v.varValue} of {v.name}")

# The optimised objective function value is printed to the screen
print("\nutility func value = ", value(problem.objective))
