from scipy.optimize import linprog

#x= [x01, x02, x13, x14, x23, x24, x34, x35, x45]
c = [  1,   5,   3,   7,   1,   6,   3,   6,   3]

A = [[ 1, 1, 0, 0, 0, 0, 0, 0, 0], # [Node0] x01 + x02  = 6
     [-1, 0, 1, 1, 0, 0, 0, 0, 0], # [Node1] x13 + x14 - x01 = 4
     [ 0,-1, 0, 0, 1, 1, 0, 0, 0], # [Node2] x23 + x24 - x02 = 2
     [ 0, 0,-1, 0,-1, 0, 1, 1, 0], # [Node3] x34 + x35 - x13 - x23 = -2
     [ 0, 0, 0,-1, 0,-1,-1, 0, 1], # [Node4] x45 - x14 - x24 - x34 = -4
     [ 0, 0, 0, 0, 0, 0, 0,-1,-1]] # [Node5] -x35 + -x45  = -6

#     n0  n1  n2  n3  n4  n5
b = [  6,  4,  2, -2, -4, -6]

# Define the bounds for each variable in the problem
x01_bnds = (0, 8)
x02_bnds = (0, 6)
x13_bnds = (0, 6)
x14_bnds = (0, 1)
x23_bnds = (0, 3)
x24_bnds = (0, 4)
x34_bnds = (0, 6)
x35_bnds = (0, 4)
x45_bnds = (0, 6)

# Solve the linear programming problem
result = linprog(c, A_eq=A, b_eq=b, bounds=( x01_bnds, x02_bnds, x13_bnds, x14_bnds,
                 x23_bnds, x24_bnds,x34_bnds, x35_bnds, x45_bnds), method='simplex')

print("The optimal solution for the flow of each link is the following:")
sol = result.x
links = [
    ('node_0', 'node_1'),
    ('node_0', 'node_2'),
    ('node_1', 'node_3'),
    ('node_1', 'node_4'),
    ('node_2', 'node_3'),
    ('node_2', 'node_4'),
    ('node_3', 'node_4'),
    ('node_3', 'node_5'),
    ('node_4', 'node_5'),
]

for i, edge in enumerate(links):
    print("Link: ", links[i], "Optimal flow:", sol[i])
