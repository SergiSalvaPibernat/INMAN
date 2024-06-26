import sys
import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt

np.set_printoptions(linewidth=150)
np.set_printoptions(suppress=True)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x) if x%1 else "{0:0.0f}".format(x)})

sys.path.append('../env')
from b_srv_1_reqsize_1 import DataCenter

discount_rate = 0.99
learning_rate = 0.01
epsilon       = 0.1        # 0.1
n_steps       = 2000000    # 2.000.000
load_Q        = False

env = DataCenter()

# Q shape (4,11,2):
Q = np.full((env.n_req_types, env.srv_size+1, env.n_actions), 0.0)

if load_Q:
    Q = np.load("../model/b_srv_1_reqsize_1_QLearn_Q.npy")

def epsilon_greed_policy(epsilon, s):
    if rnd.random() > epsilon:
        return np.argmax(Q[s[0],s[1]])
    else:
        return rnd.choice(env.n_actions)

def plot_a_2D_DataCenter():
    state_res = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    state_req = [0, 1, 2, 3]
    n_state_res = len(state_res)
    n_state_req = len(state_req)
    states = np.zeros((n_state_res * n_state_req, 2), dtype=int)

    a = np.zeros((n_state_res * n_state_req, 1))
    q = np.zeros((n_state_res * n_state_req, 1))

    index = 0
    for index_state_req in range(n_state_req):
        for index_state_res in range(n_state_res):
            states[index, :] = state_req[index_state_req], state_res[index_state_res]
            index += 1

    q_s_a = np.zeros((len(states), 2))
    for index_state in range(len(states)):
        q_s_a[index_state] = Q[states[index_state][0], states[index_state][1], :]

    for index in range(n_state_res * n_state_req):
        a[index, :] = np.argmax(q_s_a[index])
        q[index, :] = q_s_a[index][int(a[index])]

    fig = plt.figure("a_2D")
    x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y2 = [1, 2, 3, 4]
    X2, Y2 = np.meshgrid(x2, y2)
    plt.scatter(np.ravel(X2), np.ravel(Y2), s=128, c=np.ravel(a))
    plt.title("QLearn a function")
    plt.xlabel("free servers")
    plt.ylabel("inverted priority")

    plt.show()
    plt.close("all")
def plot_q_a_1D_DataCenter():
    state_res = [0, 1, 2, 3, 4, 5, 6]  # , 7, 8, 9, 10]
    state_req = [0, 1, 2, 3]
    n_state_res = len(state_res)
    n_state_req = len(state_req)
    states = np.zeros((n_state_res, 2), dtype=int)

    a = np.zeros((n_state_req, n_state_res, 1))
    q = np.zeros((n_state_req, n_state_res, 1))

    for index_state_req in range(n_state_req):

        for index_state_res in range(n_state_res):
            states[index_state_res, :] = state_req[index_state_req], state_res[index_state_res]

        q_s_a = np.zeros((len(states), 2))
        for index_state in range(len(states)):
            q_s_a[index_state] = Q[states[index_state][0], states[index_state][1], :]

        for index in range(n_state_res):
            a[index_state_req, index, 0] = np.argmax(q_s_a[index])
            q[index_state_req, index, 0] = q_s_a[index][int(a[index_state_req, index, 0])]

    fig = plt.figure("q_1D")
    plt.suptitle("QLearn q function")

    colors = ["blue", "green", "yellow", "red"]
    for index_state_req in range(n_state_req):
        plt.plot(state_res, q[index_state_req], c=colors[index_state_req])
    plt.xlabel('free servers')

    fig2 = plt.figure("a_1D")
    plt.suptitle("QLearn a function")

    for index_state_req in range(n_state_req):
        plt.plot(state_res, a[index_state_req], c=colors[index_state_req])
    plt.xlabel('free servers')

    plt.show()
    plt.close("all")

s = env.reset()

r_avg = 0
discarded = np.zeros((env.n_req_types))
accepted  = np.zeros((env.n_req_types))
rejected  = np.zeros((env.n_req_types))
empty_slots = np.zeros((env.srv_size + 1))

for step in range(n_steps):

    req_type = s[0]
    num_empty_slots = s[1]

    a = epsilon_greed_policy(epsilon, s)  # epsilon greed policy

    empty_slots[num_empty_slots] += 1

    if a == 0:
        if num_empty_slots == 0:
            rejected[req_type] += 1
        else:
            accepted[req_type] += 1

    if a == 1:
        discarded[req_type] += 1

    # to be completed

    s = s_  # move to next state

np.save("../model/b_srv_1_reqsize_1_QLearn_Q", Q)

print('r_avg = %.4f' % (r_avg * sum(env.req_val)) )
print('full  = %.4f' % (empty_slots[0] / n_steps))
print('discarded = %.4f' % (sum(discarded) / n_steps) )
print('rejected  = %.4f' % (sum(rejected) / n_steps) )
print('accepted  = %.4f' % (sum(accepted) / n_steps) )
print('dis_rate  = ', discarded / n_steps)
print('rej_rate  = ', rejected / n_steps)
print('acc_rate  = ', accepted / n_steps)
print('empty slots = ', empty_slots / n_steps)
#print(' ')
#print(Q)

plot_a_2D_DataCenter()
#plot_q_a_1D_DataCenter()






