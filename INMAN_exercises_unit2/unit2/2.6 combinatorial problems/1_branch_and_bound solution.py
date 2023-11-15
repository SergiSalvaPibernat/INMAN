from scipy.optimize import linprog

class IP_solver:

    def __init__(self):
        self.min = 100
        self.x   = [0,0]

    def LP_solving(self, x0_bnds, x1_bnds):
        c = [-8, -5]
        A = [[1, 1], [9, 5]]
        b = [6, 45]
        res = linprog(c, A, b, bounds=(x0_bnds, x1_bnds), method="simplex")
        return res

    def IP_solving(self, x0_bnds, x1_bnds):

        res = self.LP_solving(x0_bnds, x1_bnds)

        if not res.success or res.fun > self.min:
            return

        if abs(int(res.x[0]) - res.x[0]) > 0.01:
            res_left  = self.IP_solving((int(res.x[0]+1), x0_bnds[1]),(0, x1_bnds[1]))
            res_right = self.IP_solving((0, int(res.x[0])), (0, x1_bnds[1]))

        else:
            if abs(int(res.x[1]) - res.x[1]) > 0.01:
                res_left  = self.IP_solving((res.x[0], x0_bnds[1]), (int(res.x[1]+1), x1_bnds[1]))
                res_right = self.IP_solving((res.x[0], x0_bnds[1]), (0, int(res.x[1])))

            else:
                if res.fun < self.min:
                    self.min = res.fun
                    self.x   = res.x
                else:
                    return

if __name__ == "__main__":

    ip = IP_solver()
    ip.IP_solving((0, None), (0, None))
    print("optimal value: ", ip.min, ", solution: ", ip.x)



