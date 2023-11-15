from scipy.optimize import linprog

#From 0 to 5: Path1 (0-1-4-5), Path2 (0-2-3-5), Path3 (0-1-3-5), Path4 (0-2-4-5), Path5 (0-1-3-4-5)
#From 1 to 4: Path6 (1-4), Path7 (1-3-4)
#From 2 to 3: Path8 (2-3)

# Define the cost for each path
cost_path_1 = 1 + 7 + 3         #Path1 (0-1-4-5)
cost_path_2 = 5 + 1 + 6         #Path2 (0-2-3-5)
cost_path_3 = 1 + 3 + 6         #Path3 (0-1-3-5)
cost_path_4 = 5 + 6 + 3         #Path4 (0-2-4-5)
cost_path_5 = 1 + 3 + 3 + 3     #Path5 (0-1-3-4-5)
cost_path_6 = 7                 #Path6 (1-4)
cost_path_7 = 3 + 3             #Path7 (1-3-4)
cost_path_8 = 1                 #Path8 (2-3)
c = [cost_path_1, cost_path_2, cost_path_3, cost_path_4, cost_path_5, cost_path_6, cost_path_7, cost_path_8]

# Define the capacity for each path
capacity_path_1 = min(8, 1, 6)         #Path1 (0-1-4-5)
capacity_path_2 = min(6, 3, 4)         #Path2 (0-2-3-5)
capacity_path_3 = min(8, 6, 4)         #Path3 (0-1-3-5)
capacity_path_4 = min(6, 4, 6)         #Path4 (0-2-4-5)
capacity_path_5 = min(8, 6, 6, 6)      #Path5 (0-1-3-4-5)
capacity_path_6 = 1                    #Path6 (1-4)
capacity_path_7 = min(6, 6)            #Path7 (1-3-4)
capacity_path_8 = 3                    #Path8 (2-3)
capacities = [capacity_path_1, capacity_path_2, capacity_path_3, capacity_path_4, capacity_path_5,
              capacity_path_6, capacity_path_7, capacity_path_8]

# Define the equality matrix
A = [[  1,  1,  1,  1,  1,  0,  0,  0],  # supply from node 0
     [  0,  0,  0,  0,  0,  1,  1,  0],  # supply from node 1
     [  0,  0,  0,  0,  0,  0,  0,  1],  # supply from node 2
     [ -1, -1, -1, -1, -1,  0,  0,  0],  # demand at node 5
     [  0,  0,  0,  0,  0, -1, -1,  0],  # demand at node 4
     [  0,  0,  0,  0,  0,  0,  0, -1]]  # demand at node 3

# Define the equality vector
b = [6, 4, 2, -6, -4, -2]

# Define the bounds for each variable (path)
path1_bnds = (0, capacity_path_1)
path2_bnds = (0, capacity_path_2)
path3_bnds = (0, capacity_path_3)
path4_bnds = (0, capacity_path_4)
path5_bnds = (0, capacity_path_5)
path6_bnds = (0, capacity_path_6)
path7_bnds = (0, capacity_path_7)
path8_bnds = (0, capacity_path_8)

# Solve the linear program
result = linprog(c, A_eq=A, b_eq=b, bounds=(path1_bnds, path2_bnds, path3_bnds, path4_bnds, path5_bnds,
                                            path6_bnds, path7_bnds, path8_bnds), method='simplex')

print("Optimal Solution:")
sol = result.x
paths = [
    ("Path 1 [0,1,4,5]"),
    ("Path 2 [0,2,3,5]"),
    ("Path 3 [0,1,3,5]"),
    ("Path 4 [0,2,4,5]"),
    ("Path 5 [0,1,3,4,5]"),
    ("Path 6 [1,4]"),
    ("Path 7 [1,3,4]"),
    ("Path 8 [2,3]"),
]

for i, edge in enumerate(paths):
    if (sol[i]>0):
        print("Link: ", paths[i], "Flow:", sol[i])