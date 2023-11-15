from pulp import *

"""Solving the knapsack problem using a MIP solver."""

# using a dictionary as the input data of the problem:
data = {"weight": [4, 3, 5],
        "value": [11, 7, 12],
        "bin_cap": 10 }
assert len(data["weight"]) == len(data["value"])


ITEMs = range(len(data["weight"]))

# max problem:
problem = LpProblem("Knapsack_Problem", LpMaximize)

# dictionary of integer variables:
var = LpVariable.dicts('Fit', ITEMs, lowBound=0, cat=LpInteger)

# utility function:
problem += lpSum([var[item]
                  * data["value"][item]
                  for item in ITEMs])

# constraint:
problem += lpSum([var[item]
                  * data["weight"][item]
                  for item in ITEMs]) <= data["bin_cap"]

problem.solve()

print(f"Status: {LpStatus[problem.status]}\n")

used_cap = 0.0

print("Used ITEMs:")
for item, var in enumerate(problem.variables()):
    if var.varValue > 0:
        print(f"{var.varValue} of item_{ITEMs[item]}")
        used_cap += var.varValue * data["weight"][item]

print(f"\nUsed capacity: {used_cap} / {data['bin_cap']}.0")
print(f"Total Profit: {value(problem.objective)}")
