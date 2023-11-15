from pulp import *

#max problem
problem = LpProblem("Knapsack_Problem", LpMaximize)

# Variables:
x1 = LpVariable("item_0", 0, None, LpInteger)
x2 = LpVariable("item_1", 0, None, LpInteger)
x3 = LpVariable("item_2", 0, None, LpInteger)

#utility function:
problem += 11 * x1 + 7 * x2 + 12 * x3

#constraint:
problem += 4 * x1 + 3 * x2 + 5 * x3 <= 10

#Solving the problem
problem.solve()

#Print the status of the solution
print(f"Status: {LpStatus[problem.status]}\n")

#Print each of the variables with the optimal value
for i in problem.variables():
    print(f"{i.varValue} of {i.name}")

#Print the optimized objective function value
print(f"\nUtility function value = {value(problem.objective)}")