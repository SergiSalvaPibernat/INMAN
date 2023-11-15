from pulp import *

#min: z = 4x01 + 3x02 + 2x13 + 2x14 + 8x23 + 2x24 + 2x35 + 2x45
# x01 + x02 <= 1
# x13 + x14 <= x01
# x23 + x24 <= x02
# x14 + x24 <= x45
# x13 + x23 <= x35
# x35 + x45 <= 1

#min problem
problem = LpProblem("Knapsack_Problem", LpMinimize)

# Variables:
x01 = LpVariable("link_0_1", 0, 1, LpInteger)
x02 = LpVariable("link_0_2", 0, 1, LpInteger)
x13 = LpVariable("link_1_3", 0, 1, LpInteger)
x14 = LpVariable("link_1_4", 0, 1, LpInteger)
x23 = LpVariable("link_2_3", 0, 1, LpInteger)
x24 = LpVariable("link_2_4", 0, 1, LpInteger)
x35 = LpVariable("link_3_5", 0, 1, LpInteger)
x45 = LpVariable("link_4_5", 0, 1, LpInteger)
#utility function:
problem += 4 * x01 + 3 * x02 + 2 * x13 + 2 * x14 + 8 * x23 + 2 * x24 + 2 * x35 + 2 * x45

#constraint:
problem += x01 + x02 == 1
problem += x01 + x02 == x01
problem += x23 + x24 == x02
problem += x14 + x24 == x45
problem += x13 + x23 == x35
problem += x35 + x45 == 1

#Solving the problem
problem.solve()

#Print the status of the solution
print(f"Status: {LpStatus[problem.status]}\n")

#Print each of the variables with the optimal value
for i in problem.variables():
    print(f"{i.varValue} of {i.name}")

#Print the optimized objective function value
print(f"\nUtility function value = {value(problem.objective)}")