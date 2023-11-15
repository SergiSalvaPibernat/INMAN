from scipy.optimize import linprog


#min: z = 4x01 + 3x02 + 2x13 + 2x14 + 8x23 + 2x24 + 2x35 + 2x45
c = [4, 3, 2, 2, 8, 2, 2, 2]
#x01 + x02 = 1
#x13 + x14 = x01
#x23 + x24 = x02
#x35 = x13 + x23
#x45 = x14 +x24
#1 = x35 + x45
# A[node][link] (input flow == output flow, for each node)
A = [[ 1,  1,  0,  0,  0,  0,  0,  0],  # Node 0
     [-1,  0,  1,  1,  0,  0,  0,  0],  # Node 1
     [ 0, -1,  0,  0,  1,  1,  0,  0],  # Node 2
     [ 0,  0, -1,  0, -1,  0,  1,  0],  # Node 3
     [ 0,  0,  0, -1,  0, -1,  0,  1],  # Node 4
     [ 0,  0,  0,  0,  0,  0, -1, -1]]  # Node 5
# b[node] (net flow of each node)
b = [1, 0, 0, 0, 0, -1]  # Node 0 has outflow of 1 unit, Node 5 has inflow of 1 unit
# Bounds for each link (can be 0 or 1)
x_bnds = [(0, 1)] * len(c)
# Solve the problem
result = linprog(c, A, b, bounds=x_bnds, method="simplex")
print(result)

