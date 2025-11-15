# random_baseline.py

import random
from snake_env import SnakeEnv

ACTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]

num_episodes = 200
max_steps_per_episode = 200

rewards_per_episode = []
foods_per_episode = []
steps_per_episode = []


def manhattan_distance(state):
    head_x, head_y, food_x, food_y = state
    return abs(head_x - food_x) + abs(head_y - food_y)


env = SnakeEnv(grid_size=10)

for episode in range(num_episodes):
    state = env.reset()
    done = False
    total_reward = 0.0
    steps = 0
    foods_eaten = 0

    for step in range(max_steps_per_episode):
        # RANDOM ACTION: no learning, no Q-table
        action = random.choice(ACTIONS)

        next_state, reward, done = env.step(action)

        # we don't do reward shaping here, just use raw reward
        if reward >= 1:
            foods_eaten += 1

        steps += 1
        total_reward += reward

        state = next_state

        if done:
            break

    rewards_per_episode.append(total_reward)
    foods_per_episode.append(foods_eaten)
    steps_per_episode.append(steps)

# compute averages over all episodes
avg_reward = sum(rewards_per_episode) / len(rewards_per_episode)
avg_foods = sum(foods_per_episode) / len(foods_per_episode)
avg_steps = sum(steps_per_episode) / len(steps_per_episode)

print("=== RANDOM AGENT BASELINE (no learning) ===")
print(f"Episodes: {num_episodes}")
print(f"Average reward: {avg_reward:.2f}")
print(f"Average foods eaten: {avg_foods:.2f}")
print(f"Average steps survived: {avg_steps:.2f}")
