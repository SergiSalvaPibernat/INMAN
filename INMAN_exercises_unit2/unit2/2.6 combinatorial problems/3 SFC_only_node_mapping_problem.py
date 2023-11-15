
"""Solve a SFC_only_node_mapping_Problem using a MIP solver."""

from pulp import *

'''
3 types of SFC:
 
        VNF1_1 -  VNF1_2  -  VNF1_3
                  
        VNF2_4 -  VNF2_5  -  VNF2_7
               \  VNF2_6  /
                     
                  VNF3_9  - VNF3_11
               /  
        VNF3_8
               \
                  VNF3_10 - VNF3_12

problem input:                        
- a given amount of requests of the 3 types of SFCs,
- the 3 SFC-graphs with their VNFs weights, 
- a set of servers of 2 types: edge-servers and core-servers.

'''

i = float("Inf")


def main():
    
    # using a dictionary as the input data of the problem:
    
    data = {
            "reqs": 6,
            "sfc_type": [0, 0, 0, 1, 1, 2],

            "vnfs": 12,
            "vnf_weight": [1, 1, 1,    1, 1, 1, 1,     1, 1, 1, 1, 1],
            "vnf_in_sfc": [
                [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            ],
        
            "srv_nodes": 3,
            "srv_type": [ 1,  1,  0], # 1: edge-server, 0: core-server
            "srv_cap":  [10, 10, 10]
            }

    REQs = range(data["reqs"])
    VNFs = range(data["vnfs"])
    SRVs = range(data["srv_nodes"])

    # min problem:
    problem = LpProblem("SFC_only_node_mapping_Problem", LpMinimize)

    # binary variables:
    var = LpVariable.dicts("vnf_fit", (REQs, VNFs, SRVs), 0, 1, LpInteger)

    # utility function: minimize the amount of vnfs of all reqs of their sfc_type to be put in SRVs of type 1:
    # to be completed

    # constraints:

    # for each srv, all allocated vnfs must not exceed the srv capacity:
    # to be completed

    # for each req, for each vnf, the vnf must be put in a single srv:
    # to be completed

    problem.solve()

    # The status of the solution is printed to the screen:
    print(f"Status: {LpStatus[problem.status]}\n")

    # print out the VNFs allocated at each server:
    total_vnfs = 0
    total_weight = 0
    for srv in SRVs:

        print(f"Content of srv_{srv}:")
        srv_weight = 0
        for req in REQs:
            for vnf in VNFs:
                if var[req][vnf][srv].value() == 1.0:
                    print(f"req_{req}_vnf_{vnf}")
                    srv_weight += data["vnf_weight"][vnf]
                    total_vnfs += 1

        print(f"weight of srv_{srv} = {srv_weight}\n")
        total_weight += srv_weight

    print(f"total accepted vnfs = {total_vnfs}")
    print(f"total weight of REQs = {total_weight}")


if __name__ == "__main__":
    main()