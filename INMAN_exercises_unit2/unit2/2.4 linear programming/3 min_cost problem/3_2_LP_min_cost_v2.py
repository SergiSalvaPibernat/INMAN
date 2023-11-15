from scipy.optimize import linprog

cap = [
[0, 8, 6, 0, 0, 0],
[0, 0, 0, 6, 1, 0],
[0, 0, 0, 3, 4, 0],
[0, 0, 0, 0, 6, 4],
[0, 0, 0, 0, 0, 6],
[0, 0, 0, 0, 0, 0]
]

cost = [
[0, 1, 5, 0, 0, 0],
[0, 0, 0, 3, 7, 0],
[0, 0, 0, 1, 6, 0],
[0, 0, 0, 0, 3, 6],
[0, 0, 0, 0, 0, 3],
[0, 0, 0, 0, 0, 0]
]

# b[node] (net flow of each node):
b = [9, 0, 0, 0, 0, -9]

# x = [x01, x02, x13, x14, x23, x24, x34, x35, x45]
c    = []
bnds = []
link  = {}
link_id = 0
num_nodes = len(cost)

for node in range(num_nodes):
    for other_node in range(num_nodes):
        if cap[node][other_node] != 0:
            c.append(cost[node][other_node])
            bnds.append((0, cap[node][other_node]))
            link[(node, other_node)] = link_id
            link_id += 1

num_links = len(c)

A = [[0 for _ in range(num_links)] for _ in range(num_nodes)]

for node in range(num_nodes):
    for other_node in range(num_nodes):
        if cap[node][other_node] != 0:
            A[node][link[(node, other_node)]] = 1
        if cap[other_node][node] != 0:
            A[node][link[(other_node, node)]] = -1

print("\nIdentified links (variables of the linear system):")
for link_id in range(num_links):
    print("link_id:", link_id, "for:", list(link.keys())[list(link.values()).index(link_id)])
print("\nSystem of linear equations: ")
print("\nc: ", c)
print("\nbnds: ", bnds)
print("\nconstraints per node, of all incoming and outgoing links from that node: A[node][link] ")
for node in range(num_nodes):
    print(A[node])
print("with net flow of each node as b: ", b)

res = linprog(c, A_eq=A, b_eq=b, bounds=bnds, method="simplex")
#print(res)

print("\nRESULTANT throughput link by link:")
for link_id in range(num_links):
    print("link: ", list(link.keys())[list(link.values()).index(link_id)], " throughput: ", res.x[link_id])