import numpy as np
import numpy.random as rnd

# states:  (A,B,C,D,E,T)
num_states = 6
print("num_states: ", num_states)
# actions: (Left, Right)
num_actions = 2
print("num_actions: ", num_actions)

P = np.array([
    [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0]],
    [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0]],
    [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0]],
    [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0]],
    [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]],
    [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
])

R = np.array([
    [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
    [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
    [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
    [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
    [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]],
    [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
])

Q = np.full((num_states, num_actions), 0.5)
Q[5,0] = 0.0
Q[5,1] = 0.0

def epsilon_greed_policy(epsilon, s):
    if rnd.random() > epsilon:
        return np.argmax(Q[s])
    else:
        return rnd.choice(num_actions)

###################################################

discount_rate = 1.00
learning_rate = 0.01
epsilon       = 0.3
n_steps       = 50000

s = 2  # start in state C
a = epsilon_greed_policy(epsilon, s)  # epsilon greed policy

# SARSA algorithm
for step in range(n_steps):

    # to be completed
    pass

print("\nQ(s,a): ")
print(Q)
print("\noptimal policy:", np.argmax(Q, axis=1), ", a to be taken from each state")



