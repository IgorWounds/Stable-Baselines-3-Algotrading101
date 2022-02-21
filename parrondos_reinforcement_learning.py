#!/usr/bin/env python

import gym
from gym import spaces
import numpy as np
import random as rn


class ParrondosEnv(gym.Env):
    """Custom Environment that follows gym interface"""

    metadata = {"render.modes": ["human"]}

    def __init__(self):
        super(ParrondosEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.win = 1000
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(high=np.inf, low=-np.inf, shape=(3, ), dtype=np.float32)

    def step(self, action):

        if action == 0:
            self.game = 0
            if rn.random() <= 0.4999999999999999999999999999:
                self.money = self.money + 1
                self.outcome = 1
            else:
                self.money = self.money - 1
                self.outcome = 0

        else:
            self.game = 1

            if self.money % 3 == 0:
                if rn.random() <= 0.1:
                    self.money = self.money + 1
                    self.outcome = 1

                else:
                    self.money = self.money - 1
                    self.outcome = 0

            else:
                if rn.random() <= 0.7499999999999999999999:
                    self.money = self.money + 1
                    self.outcome = 1

                else:
                    self.money = self.money - 1
                    self.outcome = 0

        self.past_games.append(self.game)

        self.prev_money = self.money

        if self.money >= self.win:
            
            self.reward = 100000000
            
            with open('pattern.txt', 'w') as f:
                f.write(str(self.past_games))

            self.money = 5
            self.finished = True

        if self.prev_money > self.money:
            self.reward = (self.money - self.prev_money) - 10

        if self.money < 1:
            self.reward = -100000000
            self.money = 5
            self.finished = True

        self.reward = (self.money / self.win) * 100

        self.observation = [self.money, self.outcome, self.game]
        self.observation = np.array(self.observation)

        self.info = {}

        return self.observation, self.reward, self.finished, self.info

    def reset(self):
        self.finished = False
        self.money = 5
        self.game = 0
        self.outcome = 0
        self.past_games = []

        self.observation = [self.money, self.outcome, self.game]
        self.observation = np.array(self.observation)

        return self.observation  # reward, done, info can't be included

    def close(self):
        print(self.money)