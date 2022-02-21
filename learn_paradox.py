#!/usr/bin/env python

import os
import time
from parrondos_reinforcement_learning import ParrondosEnv
from stable_baselines3 import PPO


model_dir = f"models/{int(time.time())}"
logs = f"logs/{int(time.time())}"

if not os.path.exists(model_dir):
    os.makedirs(model_dir)

if not os.path.exists(logs):
    os.makedirs(logs)

env = ParrondosEnv()
env.reset()

model = PPO("MlpPolicy", env, verbose=1, device="cuda", tensorboard_log=logs)

STEPS = 10000

for i in range(1, 10):
    model.learn(STEPS, reset_num_timesteps=False, tb_log_name="PPO")
    model.save(f"{model_dir}/{STEPS}")

env.close()

