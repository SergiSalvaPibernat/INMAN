
import copy
import numpy as np

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.num_nodes = len(graph)
        self.parent = [-1] * (self.num_nodes)
        self.visited = [False] * self.num_nodes
        self.path = []
        self.all_paths = []

    def path_flow(self, path):

        path_flow = float("Inf")

        for index in range(len(path)-1):
            path_flow = min(path_flow, g.graph[path[index]][path[index + 1]])

        return path_flow

    def residual_cap(self, path, path_flow):

        for index in range(len(path) - 1):
            g.graph[path[index]][path[index + 1]] -= path_flow

    def kShortestPaths(self, src, dst, k, BW):

        self.k_shortest_paths = []
        self.shortest_path_bw = []

        queue = []
        counter = 0

        queue.append([src])

        while queue and counter < k:

            s_path = queue.pop(0)
            u = s_path[-1]

            for v, capacity in enumerate(self.graph[u]):
                if capacity > 0:
                    new_path = copy.deepcopy(s_path)
                    new_path.append(v)
                    if v == dst:
                        self.k_shortest_paths.append(new_path)
                        counter = counter + 1
                        path_flow = self.path_flow(new_path)
                        if path_flow >= BW:
                            return new_path, BW
                        else:
                            self.shortest_path_bw.append(path_flow)
                    else:
                        queue.append(new_path)

        if len(self.k_shortest_paths) != 0:
            index = np.argmax(self.shortest_path_bw)
            return self.k_shortest_paths[index], self.shortest_path_bw[index]
        else:
            return [], 0


if __name__ == "__main__":

    cap = [
        [0, 8, 6, 0, 0, 0],
        [0, 0, 0, 6, 1, 0],
        [0, 0, 0, 3, 4, 0],
        [0, 0, 0, 0, 6, 4],
        [0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0]
    ]

    g = Graph(cap)

    source = 0
    sink   = 5
    k      = 10
    BW     = 4

    path, path_bw = g.kShortestPaths(source, sink, k, BW)
    if len(path) == 0:
        print("no single path for: (", source, ",", sink, ") with BW =", BW)

    else:
        print("the path: ", path, " with flow: ", path_bw)
        g.residual_cap(path, path_bw)

        source = 1
        sink   = 4
        k      = 10
        BW     = 4

        path, path_bw = g.kShortestPaths(source, sink, k, BW)
        if len(path) == 0:
            print("no single path for: (", source, ",", sink, ") with BW =", BW)

        else:
            print("the path: ", path, " with flow: ", path_bw)
            g.residual_cap(path, BW)

            source = 2
            sink   = 3
            k      = 10
            BW     = 2

            path, path_bw = g.kShortestPaths(source, sink, k, BW)
            if len(path) == 0:
                print("no single path for: (", source, ",", sink, ") with BW =", BW)

            else:
                print("the path: ", path, " with flow: ", path_bw)
                g.residual_cap(path, BW)
