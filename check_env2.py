#!/usr/bin/env python

from parrondos_reinforcement_learning import ParrondosEnv

env = ParrondosEnv()
episodes = 3

for episode in range(episodes):
    done = False
    obs = env.reset()
    while not done:
        random_action = env.action_space.sample()
        print(f"action: {random_action}")
        obs, reward, done, info = env.step(random_action)
        print(f"reward: {reward}\nobservation: {obs}")
