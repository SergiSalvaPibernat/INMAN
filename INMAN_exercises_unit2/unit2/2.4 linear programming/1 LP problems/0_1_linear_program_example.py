from scipy.optimize import linprog

# min: z = -x0 + 4x1
# subject to:
# -3x0 +  x1 <=  6
#   x0 + 2x1 <=  4
#         x1 => -3

c = [-1, 4]
A = [[-3, 1], [1, 2]]
b = [6, 4]

x0_bnds = (None, None)
x1_bnds = (-3, None)

result = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bnds, x1_bnds), method="simplex")

print(result)