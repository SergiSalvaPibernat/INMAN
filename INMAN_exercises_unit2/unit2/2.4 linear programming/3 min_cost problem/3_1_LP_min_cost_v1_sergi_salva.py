from scipy.optimize import linprog
# Same stategy as LP Prolblems plroblem 0_1_linear_program_example

#cost[link] (each link is a variable of the LP problem)
#x  [x01, x02, x13, x14, x23, x24, x34, x35, x45]
c = [1, 5, 3, 7, 1, 6, 3, 6, 3]

# A[node][link] (input flow == output flow, for each node):
A = [[ 1,  1,  0,  0,  0,  0,  0,  0,  0],  #Node 0
     [-1,  0,  1,  1,  0,  0,  0,  0,  0],  #Node 1
     [ 0, -1,  0,  0,  1,  1,  0,  0,  0],  #Node 2
     [ 0,  0, -1,  0, -1,  0,  1,  1,  0],  #Node 3
     [ 0,  0,  0, -1,  0, -1, -1,  0,  1],  #Node 4
     [ 0,  0,  0,  0,  0,  0,  0, -1, -1]] #Node 5
     #01, 02, 13, 14, 23, 24, 34, 35, 45

# b[node] (net flow of each node)
   #n0, n1, n2, n3, n4, n5
b = [9,  0,  0,  0,  0, -9]

#links (variables) bounds:
x01_bnds = (0, 8)
x02_bnds = (0, 6)
x13_bnds = (0, 6)
x14_bnds = (0, 1)
x23_bnds = (0, 3)
x24_bnds = (0, 4)
x34_bnds = (0, 6)
x35_bnds = (0, 4)
x45_bnds = (0, 6)
# Solve the problem
result = linprog(c, A_eq=A, b_eq=b, bounds=(x01_bnds, x02_bnds, x13_bnds, x14_bnds, x23_bnds, x24_bnds, x34_bnds,
                                  x35_bnds, x45_bnds), method="highs")

print("The optimal solution to obtain the min cost is the following:")
sol = result.x
links = [('node_0', 'node_1'),
         ('node_0', 'node_2'),
         ('node_1', 'node_3'),
         ('node_1', 'node_4'),
         ('node_2', 'node_3'),
         ('node_2', 'node_4'),
         ('node_3', 'node_4'),
         ('node_3', 'node_5'),
         ('node_4', 'node_5'),]

for i, edge in enumerate(links):
    print("Link: ", links[i], "Optimal flow:", sol[i])
