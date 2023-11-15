
"""Solve an SFC_Problem using a MIP solver."""

from pulp import *

'''

3 types of SFC:
                   ----    VNF1_1 -  VNF1_2  -  VNF1_3
                  /
                 / ----    VNF2_4 -  VNF2_5  -  VNF2_7
                /                 \  VNF2_6  /
               /      
        VNF_0                        VNF3_9  -  VNF3_11
               \                  /  
                  ----     VNF3_8
                                  \
                                     VNF3_10 -  VNF3_12

problem input:                        
- a given amount of requests of the 3 types of SFCs with an ingress router for each request,
- the 3 SFC-graphs with their VNFs weights, 
- a network of nodes: routers and servers of 2 types: edge-servers and core-servers.

'''

i = float("Inf")


def main():

    # using a dictionary as the input data of the problem:

    data = {
            "reqs": 6,
            "sfc_type": [0, 0, 0, 1, 1, 2], # 3 types of SFCs are defined
            "ing_node": [3, 0, 3, 0, 0, 6], # ing_nodes: {0,3,6}

            "vnfs": 13,
            "vnf_weight": [0,   1, 1, 1,    1, 1, 1, 1,    1, 1, 1, 1, 1],
            "vnf_in_sfc": [
                [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            ],
            "vnf_to_vnf": [
                [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],

            "nodes": 8,
            "srv_node": [0, 0,  1, 0, 0,  1, 0,  1],  # {2,5,7}
            "srv_type": [0, 0,  1, 0, 0,  1, 0,  0],  # edge_nodes: {2,5}, core_nodes: {7}
            "srv_cap":  [0, 0,  5, 0, 0,  5, 0, 15],
            "nde_to_nde":
                [[0, 1, 1, 1, 0, 0, 0, 0],
                 [1, 0, 1, 0, 1, 1, 0, 0],
                 [1, 1, 0, 1, 0, 1, 1, 0],
                 [1, 0, 1, 0, 0, 0, 1, 0],
                 [0, 1, 0, 0, 0, 1, 0, 1],
                 [0, 1, 1, 0, 1, 0, 1, 1],
                 [0, 0, 1, 1, 0, 1, 0, 1],
                 [0, 0, 0, 0, 1, 1, 1, 0]],
            "phy_bw":
               [[ 0, 10, 10, 10,  0,  0,  0,  0],
                [10,  0, 10,  0, 10, 10,  0,  0],
                [10, 10,  0, 10,  0, 10, 10,  0],
                [10,  0, 10,  0,  0,  0, 10,  0],
                [ 0, 10,  0,  0,  0, 10,  0, 10],
                [ 0, 10, 10,  0, 10,  0, 10, 10],
                [ 0,  0, 10, 10,  0, 10,  0, 10],
                [ 0,  0,  0,  0, 10, 10, 10,  0]]
            }

    REQs = range(data["reqs"])
    VNFs = range(data["vnfs"])
    NDEs = range(data["nodes"])

    # min problem:
    problem = LpProblem("SFC_Problem", LpMinimize)

    # binary variables:
    var_vnf = LpVariable.dicts("vnf_fit", (REQs, VNFs, NDEs), 0, 1, LpInteger)
    var_lnk = LpVariable.dicts("lnk_fit", (REQs, VNFs, VNFs, NDEs, NDEs), 0, 1, LpInteger)

    # utility function: minimize the amount of vnfs of all reqs of their sfc_type to be put in SRVs of type 1 and
    #                   minimize the amount of p_links (u,v) used to map all v_links (k,k') of all reqs:
    # to be completed

    # constraints:

    # for each node, if srv, all allocated vnfs must not exceed the srv capacity:
    # to be completed

    # for each p_link (u,v), all allocated v_links (k,k') must not exceed the p_link capacity:
    # to be completed

    # flow conservation at each node_u, individually for each req, solved the MCF problem:
    # for each req, for each v_link (k,k'), for each node_u not hosting vnf_k or vnf_k', output_flow_from_u - input_flow_to_u = 0
    # for each req, for each v_link (k,k'), for each node_u hosting vnf_k,  output_flow_from_u = 1
    # for each req, for each v_link (k,k'), for each node_u hosting vnf_k', -input_flow_to_u = -1
    # for each req, for each v_link (k,k'), for each node_u hosting vnf_k and vnf_k', output_flow_from_u - input_flow_to_u = 0
    for req in REQs:
        for vnf_k in VNFs:
            for vnf_k_ in VNFs:
                if data["vnf_in_sfc"][data["sfc_type"][req]][vnf_k] == 1 and \
                   data["vnf_in_sfc"][data["sfc_type"][req]][vnf_k_] == 1 and \
                   data["vnf_to_vnf"][vnf_k][vnf_k_] == 1:
                    for node_u in NDEs:
                        problem += lpSum((var_lnk[req][vnf_k][vnf_k_][node_u][node_v] * data["nde_to_nde"][node_u][node_v] -
                                          var_lnk[req][vnf_k][vnf_k_][node_v][node_u] * data["nde_to_nde"][node_v][node_u])
                                         for node_v in NDEs) == (var_vnf[req][vnf_k][node_u] - var_vnf[req][vnf_k_][node_u])

    # for each req, for each vnf, the vnf must be put in a single nde (including VNF_0),
    # all VNFs of all REQs must be allocated:
    # to be completed

    # for each req, for each vnf different from VNF_0, the vnf must be put in a single srv_node:
    # to be completed

    # for each req, we allocate VNF_0 at the ing_node of the req,
    # all REQs must be allocated:
    # to be completed

    problem.solve()

    # The status of the solution is printed to the screen:
    print(f"Status: {LpStatus[problem.status]}\n")

    # print out the VNFs allocated at each server:
    total_vnfs = 0
    total_weight = 0
    for nde in NDEs:
        if data["srv_node"][nde] == 1:
            print(f"Content of srv_{nde}:")
            srv_weight = 0
            for req in REQs:
                for vnf in VNFs:
                    if var_vnf[req][vnf][nde].value() == 1.0:
                        print(f"req_{req}_vnf_{vnf}")
                        srv_weight += data["vnf_weight"][vnf]
                        total_vnfs += 1

            print(f"weight of srv_{nde} = {srv_weight}\n")
            total_weight += srv_weight

    print(f"total accepted vnfs = {total_vnfs}")
    print(f"total weight of requests = {total_weight}\n")

    # print out the p_links used to map all v_links of all requests:
    total_vlinks = 0
    total_plinks = 0
    for req in REQs:
        print(f"\n\nreq_{req}")
        for vnf_k in VNFs:
            for vnf_k_ in VNFs:
                if data["vnf_in_sfc"][data["sfc_type"][req]][vnf_k] == 1 and \
                   data["vnf_in_sfc"][data["sfc_type"][req]][vnf_k_] == 1 and \
                   data["vnf_to_vnf"][vnf_k][vnf_k_]:
                    total_vlinks += 1
                    print(f"\nvnf_{vnf_k}_vnf_{vnf_k_} by edges: ", end="")
                    for node_u in NDEs:
                        for node_v in NDEs:
                            if var_lnk[req][vnf_k][vnf_k_][node_u][node_v].value() == 1.0:
                                print(f"{node_u}_{node_v}, ", end="")
                                total_plinks += 1

    print(f"\n\ntotal vlinks = {total_vlinks}")
    print(f"total used plinks = {total_plinks}\n")


if __name__ == "__main__":
    main()