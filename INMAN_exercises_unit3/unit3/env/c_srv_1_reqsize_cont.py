
import numpy as np

np.set_printoptions(linewidth=150)
np.set_printoptions(suppress=True)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x) if x%1 else "{0:0.3f}".format(x)})

pi = np.pi

class DataCenter:

    def __init__(self):

        self.GRA1 = 0.6 # Guaranteed resource amount
        self.MAX1 = 0.8 # Maximum resource amount
        self.GRA2 = 0.4
        self.MAX2 = 0.8
        self.MIN  = 0.1

        self.state_res = np.zeros(5, dtype=float)
        self.USD1 = 0   # Used resources
        self.ASG1 = 1   # Assigned resources
        self.USD2 = 2
        self.ASG2 = 3
        self.FREE = 4   # Unassigned resources

        self.state_req = np.zeros(2, dtype=float)
        self.REQ1 = 0   # Requested resources
        self.REQ2 = 1

        self.n_actions  = 9 # 3x3 actions from (decrease, keep, increase)
        self.n_features = len(self.show_state())
        self.act_vector = np.zeros(2, dtype=int)

        #####################################################
        ###########  history of n complete cycles ###########
        #####################################################

        self.one_cycle   = 4000
        self.load_offset = (3.0/4.0)*pi
        self.avg_load1   = 0.40
        self.avg_load2   = 0.40
        self.min_load    = 0.1

        self.H_SIZE = 5 * self.one_cycle
        self.h_step = 0

        self.hist   = np.zeros((self.H_SIZE, 6))
        self.H_REQ1 = 0
        self.H_REQ2 = 1
        self.H_ASG1 = 2
        self.H_ASG2 = 3
        self.H_SLA  = 4
        self.H_USD  = 5

    def show_state(self):
        return np.concatenate((self.state_req, self.state_res))

    def reset(self):

        self.state_res[self.ASG1] = self.GRA1
        self.state_res[self.ASG2] = self.GRA2

        self.step_load()
        self.step_processing()

        self.h_step = 0
        self.hist = np.zeros((self.H_SIZE, 6))
        return self.show_state()

    def step(self, a):

        a1, a2 = self.act_map(a)

        if a1 == 0:
            self.state_res[self.ASG1] = max(self.MIN, self.state_res[self.ASG1] * 0.95)

        if a1 == 2:
            self.state_res[self.ASG1] = min(self.MAX1, self.state_res[self.ASG1] * 1.05)

        if a2 == 0:
            self.state_res[self.ASG2] = max(self.MIN, self.state_res[self.ASG2] * 0.95)

        if a2 == 2:
            self.state_res[self.ASG2] = min(self.MAX2, self.state_res[self.ASG2] * 1.05)

        if (self.state_res[self.ASG1] + self.state_res[self.ASG2]) > 1.0:
            dec = ((self.state_res[self.ASG1] + self.state_res[self.ASG2]) - 1.0) / 2
            self.state_res[self.ASG1] -= dec
            self.state_res[self.ASG2] -= dec

        self.step_load()
        self.step_processing()

        self.hist[self.h_step, self.H_REQ1] = self.state_req[self.REQ1]
        self.hist[self.h_step, self.H_REQ2] = self.state_req[self.REQ2]
        self.hist[self.h_step, self.H_ASG1] = self.state_res[self.ASG1]
        self.hist[self.h_step, self.H_ASG2] = self.state_res[self.ASG2]

        s_ = self.show_state()
        r = self.reward()

        self.h_step = (self.h_step + 1) % self.H_SIZE
        return s_, r

    def reward(self):

        # to be completed

        self.hist[self.h_step, self.H_SLA] = SLA_rate
        self.hist[self.h_step, self.H_USD] = USED_rate
        return reward

    def render(self):
        print("state: ", self.show_state())

    def step_load(self):

        self.state_req[self.REQ1] = self.avg_load1 * (1 + np.sin(2 * pi * (self.h_step / self.one_cycle)))
        self.state_req[self.REQ2] = self.avg_load2 * (1 + np.sin(2 * pi * (self.h_step / self.one_cycle) + self.load_offset))
        '''
        if self.h_step % int(self.one_cycle/4) == 0:
            self.load_offset += np.random.normal(0.0, pi/8.0)
        '''
        #self.state_req[self.REQ1] += np.random.normal(0.0, 0.02)
        #self.state_req[self.REQ2] += np.random.normal(0.0, 0.02)

        self.state_req[self.REQ1] = max(self.min_load, self.state_req[self.REQ1])
        self.state_req[self.REQ2] = max(self.min_load, self.state_req[self.REQ2])

    def step_processing(self):

        if self.state_req[self.REQ1] > self.state_res[self.ASG1]:
            self.state_res[self.USD1] = self.state_res[self.ASG1]
        else:
            self.state_res[self.USD1] = self.state_req[self.REQ1]

        if self.state_req[self.REQ2] > self.state_res[self.ASG2]:
            self.state_res[self.USD2] = self.state_res[self.ASG2]
        else:
            self.state_res[self.USD2] = self.state_req[self.REQ2]

        self.state_res[self.FREE] = 1.0 - (self.state_res[self.ASG1] + self.state_res[self.ASG2])

    def act_map(self, a):

        if a == 0: np.put(self.act_vector, [0, 1], [0, 0])
        if a == 1: np.put(self.act_vector, [0, 1], [1, 0])
        if a == 2: np.put(self.act_vector, [0, 1], [0, 1])
        if a == 3: np.put(self.act_vector, [0, 1], [2, 0])
        if a == 4: np.put(self.act_vector, [0, 1], [0, 2])
        if a == 5: np.put(self.act_vector, [0, 1], [1, 1])
        if a == 6: np.put(self.act_vector, [0, 1], [1, 2])
        if a == 7: np.put(self.act_vector, [0, 1], [2, 1])
        if a == 8: np.put(self.act_vector, [0, 1], [2, 2])

        return self.act_vector


if __name__ == "__main__":

    RENDER = True
    env = DataCenter()
    s   = env.reset()

    for step in range(2000):
        action = np.random.randint(0, env.n_actions)
        if RENDER:
            print("state: ", env.show_state(),
                  " a: ", action)
        s_, r = env.step(action)


