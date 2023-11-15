# adding a fictitious link from sink to source with cost -1,
# all other links of cost 0, we want to minimize the cost (maximize
# the data transmitted through the sink-to-source link.
# regarding the constraints, at all nodes the input flow equals the
# output flow: b = [0, 0, ..., 0, 0]
from scipy.optimize import linprog

c = [0, 0, 0, 0, 0, 0, -1]
# x [x01, x03, x12, x13, x24, x34, x40]
# A[node][link] (input flow == output flow, for each node):
A = [[-1,  0,  1,  1,  0,  0,  0],
     [ 0,  0, -1,  0,  1,  0,  0],
     [ 0, -1,  0, -1,  0,  1,  0],
     [ 0,  0,  0,  0, -1, -1,  1],
     [ 1,  1,  0,  0,  0,  0, -1]]
# b[node] (net flow of each node)
b = [ 0, 0, 0, 0, 0]
#links (variables) bounds:
x01_bnds = (0, 2)
x03_bnds = (0, 3)
x12_bnds = (0, 4)
x13_bnds = (0, 3)
x24_bnds = (0, 1)
x34_bnds = (0, 2)
x40_bnds = (0, None)

# Solve the problem
result = linprog(c, A, b, bounds=(x01_bnds, x03_bnds, x12_bnds, x13_bnds,
                                  x24_bnds, x34_bnds, x40_bnds), method="simplex")

print("The optimal solution for the max flow with minimum cost is the following:")
sol = result.x

links = [('node_0', 'node_1'),
         ('node_0', 'node_3'),
         ('node_1', 'node_2'),
         ('node_1', 'node_3'),
         ('node_2', 'node_4'),
         ('node_3', 'node_4'),
         ('node_4', 'node_0')]

for i, edge in enumerate(links):
    print("Link: ", links[i], "Optimal flow:", sol[i])