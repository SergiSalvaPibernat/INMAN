

"""Solve a Multi_Knapsack_Problem using a MIP solver."""

from pulp import *


def main():
    
    # using a dictionary as the input data of the problem:
    
    data = {
            "req_weight": [48, 30, 42, 36, 36, 48, 42, 42, 36, 24, 30, 30, 42, 36, 36],
            "req_value":  [10, 30, 25, 50, 35, 30, 15, 40, 30, 35, 45, 10, 20, 30, 25],
            "bin_cap":    [100, 100, 100, 100, 100]
            }
    
    assert len(data["req_weight"]) == len(data["req_value"])
 
    REQs = range(len(data["req_weight"]))
    BINs = range(len(data["bin_cap"]))

    # max problem:
    problem = LpProblem("Multi_Knapsack_Problem", LpMaximize)

    # binary variables:
    var = LpVariable.dicts("req_fit", (REQs, BINs), 0, 1, LpInteger)
    #req_fit_0_0(Request_Bin) = either 0 or 1 (put)

    # utility function: maximise the accumulated value of accepted REQs:
    # to be completed

    # constraints:
    # as many constraints as requests.
    # for each bin, all allocated reqs must not exceed the bin capacity:
    # to be completed

    # for each req, it must be put in a single bin,
    # with <= 1 we are not enforcing embedding all REQs:
    for req in REQs:
        problem += lpSum(var[req][bin]
                         for bin in BINs) <= 1
        
    problem.solve()

    # The status of the solution is printed to the screen:
    print(f"Status: {LpStatus[problem.status]}\n")

    # print out the REQs allocated at each bin:
    total_reqs = 0
    total_weight = 0
    for bin in BINs:
        print(f"Content of bin_{bin}:")
        bin_weight = 0
        for req in REQs:
            if var[req][bin].value() == 1.0:
                print(f"req_{req}")
                bin_weight += data["req_weight"][req]
                total_reqs += 1
        print(f"weight of bin_{bin} = {bin_weight}\n")
        total_weight += bin_weight
    print(f"total accepted REQs = {total_reqs}")
    print(f"total weight REQs = {total_weight}")


if __name__ == "__main__":
    main()
