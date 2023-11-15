from scipy.optimize import linprog

# max: z = 2x0 + 3x1
# subject to:
#   x0 + 2x1 <=  6
#  2x0 +  x1 <=  8
#    x0,  x1 >=  0

c = [-2, -3]
A = [[1, 2], [2, 1]]
b = [6, 8]

x0_bnds = (0, None)
x1_bnds = (0, None)

result = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bnds, x1_bnds), method="simplex")

print(result)