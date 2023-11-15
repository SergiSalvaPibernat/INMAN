import sys
import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt

np.set_printoptions(linewidth=150)
np.set_printoptions(suppress=True)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x) if x%1 else "{0:0.0f}".format(x)})

sys.path.append('../util')
from DQN import DeepQNetwork

sys.path.append('../env')
from b_srv_1_reqsize_1 import DataCenter

discount_rate = 0.99
learning_rate = 0.01   # 0.01   | to check:
epsilon       = 0.1    # 0.1    | 0.0
n_steps       = 60000  # 60000  | 40000
replace       = 1000
to_load_model = False
keep_learning = True

env = DataCenter()

DQN = DeepQNetwork(n_features=env.n_features,
                   n_actions=env.n_actions,
                   learning_rate=learning_rate,
                   reward_decay=discount_rate,
                   memory_size=2 ** 15,  # (s,a,r,s_): (4x11)x2x5x(4x11) = 19360 entries
                   batch_size =2 ** 7,  # 128
                   replace_target_iter=replace,
                   to_load_model=to_load_model,
                   name_model='b_srv_1_reqsize_1_DQN')

def epsilon_greed_policy(epsilon, s):
    if rnd.random() > epsilon:
        return DQN.choose_action(s)
    else:
        return rnd.choice(env.n_actions)

steps_to_start_learning = DQN.batch_size * 10

s = env.reset()

r_avg = 0
discarded = np.zeros((env.n_req_types))
rejected  = np.zeros((env.n_req_types))
accepted  = np.zeros((env.n_req_types))
empty_slots  = np.zeros((env.srv_size + 1))

for step in range(n_steps):

    req_type = s[0]
    num_empty_slots = s[1]

    a = epsilon_greed_policy(epsilon, s)

    # do not discard any request:
    #a = 0

    # alternative heuristic, close to optimal policy:
    # if (req_type == 0 or req_type == 1):
    #     a = 0
    # else:
    #     a = 1

    empty_slots[num_empty_slots] += 1

    if a == 0:
        if num_empty_slots == 0:
            rejected[req_type] += 1
        else :
            accepted[req_type] += 1

    if a == 1:
        discarded[req_type] += 1

    # to be completed

    s = s_  # move to next state

DQN.save_model()

print('r_avg = %.4f' % (r_avg * sum(env.req_val)) )
print('full  = %.4f' % (empty_slots[0] / n_steps))
print('discarded = %.4f' % (sum(discarded) / n_steps) )
print('rejected  = %.4f' % (sum(rejected) / n_steps) )
print('accepted  = %.4f' % (sum(accepted) / n_steps) )
print('dis_rate  = ', discarded / n_steps)
print('rej_rate  = ', rejected / n_steps)
print('acc_rate  = ', accepted / n_steps)
print('empty slots = ', empty_slots / n_steps)

DQN.plot_a_2D_DataCenter("all", True)







