
import numpy as np
import numpy.random as rnd


class DataCenter:

    def __init__(self):

        self.n_server = 1
        self.srv_size = 10
        self.req_size = 1
        self.req_val  = np.array((8, 4, 2, 1))
        self.reward   = self.req_val / sum(self.req_val)

        self.n_req_types   = len(self.req_val)
        self.prob_req_exit = 0.06

        self.state_req_type   = 0
        self.state_empty_slots = self.srv_size

        self.n_actions  = 2 # accept or reject request
        self.n_features = len(self.show_state())

    def show_state(self):
        return np.array((self.state_req_type, self.state_empty_slots))

    def reset(self):
        self.state_empty_slots = rnd.randint(0, self.srv_size + 1) # randint from [0,10]
        self.step_load()
        return self.show_state()

    def step(self, a):
        # a == 0, accept:
        if a == 0:

            # to be completed
            pass

        # a == 1, reject:
        else:

            # to be completed
            pass

        self.step_processing()
        self.step_load()

        s_ = self.show_state()
        return s_, reward

    def render(self):
        print("state: ", self.show_state())

    def step_processing(self):
        used_slots = self.srv_size - self.state_empty_slots
        for slot in range(used_slots):
            if rnd.random() < self.prob_req_exit:
                self.state_empty_slots += 1

    def step_load(self):
        self.state_req_type = rnd.randint(0, self.n_req_types)


if __name__ == "__main__":

    RENDER = True
    env = DataCenter()
    s   = env.reset()

    for step in range(100):

        a = np.random.randint(0, env.n_actions)
        if RENDER:
            print("state: ", env.show_state(), " a: ", a)
        s_, r = env.step(a)


