#!/usr/bin/env python

import gym
from stable_baselines3 import PPO

path = "models/PPO/20000.zip"

env = gym.make("LunarLander-v2")

env.reset()

model = PPO.load(path, env)

episodes = 10

for episode in range(episodes):
    observation = env.reset()
    finished = False
    while not finished:
        env.render()
        action, _ = model.predict(observation)
        obs, reward, done, info = env.step(action)

env.close()
