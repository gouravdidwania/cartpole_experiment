import gymnasium as gym
import numpy as np
import time
from tqdm import tqdm
import random

env = gym.make("CartPole-v1", render_mode="human")
print("Observational Space : ", env.observation_space)
print("Action Space:", env.action_space)


class Agent:
    def __init__(self, env1):
        self.action_size = env1.action_space.n
        # print("Action Size :", self.action_size)

    # @staticmethod
    def get_action(self, obs):
        action = random.choice(range(self.action_size))
        CartPosition, CartVelocity, PoleAngle, PoleAngularVelocity = obs[0], obs[1], obs[2], obs[3]
        # action = 0 if PoleAngle < 0 else 1
        return action


total_rewards = list()
N_episodes = 20
N_steps = 200

for episode in range(N_episodes):
    rewards = 0
    agent = Agent(env)
    observation, info = env.reset()  # observation : [CartPosition, CartVelocity, PoleAngle, PoleAngularVelocity]
    for step in tqdm(range(N_steps)):
        action = agent.get_action(observation)
        Observations, reward, done, info, _ = env.step(action)
        env.render()
        # time.sleep(0.001) # sleep
        rewards += reward
        if done:  # Fallen
            break
    print(f"Episode: {episode} and Score: {rewards}")
    total_rewards.append(rewards)

stats = {
    "mean": np.mean(total_rewards),
    "std": np.std(total_rewards),
    "min": np.min(total_rewards),
    "max": np.max(total_rewards)
}

print(stats)
