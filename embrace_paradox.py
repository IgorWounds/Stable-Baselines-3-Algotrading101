#!/usr/bin/env python

from stable_baselines3 import PPO
from parrondos_reinforcement_learning import ParrondosEnv

path = "models/1645460912/10000.zip"

env = ParrondosEnv()

env.reset()

model = PPO.load(path, env)

observation = env.reset()
pattern = []
while True:
    action, _ = model.predict(observation)
    obs, reward, done, info = env.step(action)
    pattern.append(obs[2])
    if obs[0] >= 1000:
        print(pattern[-10:])
        break

env.close()
