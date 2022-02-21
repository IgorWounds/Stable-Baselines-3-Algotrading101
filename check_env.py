#!C:\Users\igorr\anaconda3\python.exe

from stable_baselines3.common.env_checker import check_env
from parrondos_reinforcement_learning import ParrondosEnv

env = ParrondosEnv()
check_env(env)
