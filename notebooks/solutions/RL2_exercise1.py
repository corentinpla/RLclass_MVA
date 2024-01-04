import gymnasium as gym
import gymnasium.envs.toy_text.frozen_lake as fl
import numpy as np

def Q_from_V(V):
    env = gym.make('FrozenLake-v1', render_mode="ansi")
    gamma = 0.9
    Q = np.zeros((env.observation_space.n, env.action_space.n))
    for s in range(env.observation_space.n):
        for a in range(env.action_space.n):
            outcomes = env.unwrapped.P[s][a]
            for o in outcomes:
                p  = o[0]
                s2 = o[1]
                r  = o[2]
                Q[s,a] += p*(r+gamma*V[s2])
    return Q
