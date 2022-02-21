#!/usr/bin/env python

import gym
from stable_baselines3 import PPO

env = gym.make("LunarLander-v2")

model = PPO("MlpPolicy", env, verbose=1, device="cuda")
model.learn(total_timesteps=20000)

episodes = 5

for episode in range(episodes):
    env.reset()
    finished = False
    while not finished:
        env.render()
        obs, reward, done, info = env.step(env.action_space.sample())

env.close()
