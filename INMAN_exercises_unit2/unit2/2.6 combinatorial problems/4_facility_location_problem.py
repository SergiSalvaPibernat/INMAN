from scipy.optimize import linprog
#podem fer servir pulp

# to be completed: c, A and b:

# cost[city] (each city is a variable of the LP problem):
c = []

# A[city][other_city] (other_city is within 15 min. of each city):
A = []

# b[city] (for each constrain of A[city], one city must have the fire station):
b = []

# city (variables) bounds (0,1) == (on/off):
bounds = [(0,1)] * len(c)

res = linprog(c, A_eq=A, b_eq=b, bounds=bounds, method="simplex")
print(res)