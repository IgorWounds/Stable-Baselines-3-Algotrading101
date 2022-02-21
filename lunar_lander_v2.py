#!/usr/bin/env python

import gym
import os
from stable_baselines3 import PPO

model_dir = "models/PPO"
logs = "logs"

if not os.path.exists(model_dir):
    os.makedirs(model_dir)

if not os.path.exists(logs):
    os.makedirs(logs)

env = gym.make("LunarLander-v2")
env.reset()

model = PPO("MlpPolicy", env, verbose=1, device="cuda", tensorboard_log=logs)

STEPS = 20000

for i in range(1, 20):
    model.learn(STEPS, reset_num_timesteps=False, tb_log_name="PPO")
    model.save(f"{model_dir}/{STEPS}")

env.close()
