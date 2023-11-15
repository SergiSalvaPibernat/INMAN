from scipy.optimize import linprog
import numpy as np
# we do not have to add the source and destination nodes
# to solve the system of linear equations.
# nodes are: a,b,c,d and 1,2,3,4.
# links are: [a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3,c4,d1,d2,d3,d4]

#cost[link] (each link is a variable of the LP problem)
# [a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3,c4, d1, d2, d3, d4]
c=[11, 12, 18, 40, 14, 15, 13, 22, 11, 17, 19, 9, 17, 14, 20, 10]

# A[node][link] (input flow == output flow, for each node):
A = [[ 1,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],   #nodeA
     [ 0,  0,  0,  0,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0],  #nodeB
     [ 0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  0,  0,  0,  0],  #nodeC
     [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1],  #nodeD
     [ 1,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0],  #node1
     [ 0,  1,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0],  #node2
     [ 0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1,  0],  #node3
     [ 0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1]]  #node4
    #[a1, a2, a3, a4, b1, b2, b3,  b4, c1, c2, c3, c4, d1, d2, d3, d4]

# b[node] (net flow of each node)
b = [1, 1, 1, 1, 1, 1, 1, 1]

#links (variables) bounds:
xa1_bnds = (0, 1)
xa2_bnds = (0, 1)
xa3_bnds = (0, 1)
xa4_bnds = (0, 1)
xb1_bnds = (0, 1)
xb2_bnds = (0, 1)
xb3_bnds = (0, 1)
xb4_bnds = (0, 1)
xc1_bnds = (0, 1)
xc2_bnds = (0, 1)
xc3_bnds = (0, 1)
xc4_bnds = (0, 1)
xd1_bnds = (0, 1)
xd2_bnds = (0, 1)
xd3_bnds = (0, 1)
xd4_bnds = (0, 1)

# Solve the problem
result = linprog(c, A_eq=A, b_eq=b, bounds=(xa1_bnds, xa2_bnds, xa3_bnds, xa4_bnds, xb1_bnds, xb2_bnds, xb3_bnds,
                                            xb4_bnds, xc1_bnds, xc2_bnds, xc3_bnds, xc4_bnds, xd1_bnds, xd2_bnds,
                                            xd3_bnds, xd4_bnds), method="highs")
# Extract optimal solution
sol = result.x
# Reshape the solution to match the transportation matrix
trans = np.array(sol).reshape(4, 4)

# Print the assignments of agents to tasks
for i, agent in enumerate(['a', 'b', 'c', 'd']):
    assigned_tasks = [str(j + 1) for j in range(4) if trans[i, j] > 0]
    if assigned_tasks:
        print(f"{agent} agent is assigned to task: {', '.join(assigned_tasks)}")
    else:
        print(f"{agent} agent is not assigned to any tasks.")