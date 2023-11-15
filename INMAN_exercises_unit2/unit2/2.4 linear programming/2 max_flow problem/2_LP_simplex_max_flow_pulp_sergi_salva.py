from pulp import *

#max z = 2 * x01 + 3 * x03 + 4 * x12 + 3 * x13 + 1 * x24 + 2 * x34
#max problem
problem = LpProblem("Knapsack_Problem", LpMaximize)

#constraints
# x01 <= 2
# x03 <= 3
# x12 <= 4
# x13 <= 3
# x24 <= 1
# x34 <= 2
# Variables:
x01 = LpVariable("link_0_1", 0, 1, LpInteger)
x03 = LpVariable("link_0_3", 0, 1, LpInteger)
x12 = LpVariable("link_1_2", 0, 1, LpInteger)
x13 = LpVariable("link_1_3", 0, 1, LpInteger)
x24 = LpVariable("link_2_4", 0, 1, LpInteger)
x34 = LpVariable("link_3_4", 0, 1, LpInteger)

#utility function:
problem += 2 * x01 + 3 * x03 + 4 * x12 + 3 * x13 + 1 * x24 + 2 * x34

# subject to:
# [Node1] x12 + x13 - x01 = 0
# [Node2] x24 - x12 = 0
# [Node3] x34 - x13 - x03 = 0
#constraint:
problem += x12 + x13 - x01 == 0
problem += x24 - x12 == 0
problem += x34 - x13 - x03 == 0


#Solving the problem
problem.solve()

#Print the status of the solution
print(f"Status: {LpStatus[problem.status]}\n")

#Print each of the variables with the optimal value
for i in problem.variables():
    print(f"{i.varValue} of {i.name}")

#Print the optimized objective function value
print(f"\nUtility function value = {value(problem.objective)}")