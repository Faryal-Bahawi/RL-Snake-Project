# q_learning_snake.py

import random
import time
from collections import defaultdict
from snake_env import SnakeEnv

# 1. Create environment
env = SnakeEnv(grid_size=10)

# 2. Define actions
ACTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]

# 3. Q-table: maps (state, action) -> value
# Using defaultdict so unseen pairs default to 0.0
Q = defaultdict(float)

# 4. Hyperparameters
alpha = 0.1      # learning rate
gamma = 0.9      # discount factor
epsilon = 0.1    # exploration rate

# For WATCHING the snake, keep episodes small.
# When you just want to train, you can set this back to e.g. 2000.
num_episodes = 3
max_steps_per_episode = 200

# To track metrics
rewards_per_episode = []
foods_per_episode = []
steps_per_episode = []


def manhattan_distance(state):
    """Compute Manhattan distance between snake head and food."""
    head_x, head_y, food_x, food_y = state
    return abs(head_x - food_x) + abs(head_y - food_y)


def choose_action(state):
    """Epsilon-greedy policy."""
    if random.random() < epsilon:
        # explore
        return random.choice(ACTIONS)
    else:
        # exploit: choose action with highest Q-value for this state
        best_action = None
        best_value = float("-inf")

        for a in ACTIONS:
            q = Q[(state, a)]
            if q > best_value:
                best_value = q
                best_action = a

        return best_action


# 5. Training loop
for episode in range(num_episodes):
    state = env.reset()
    done = False
    total_reward = 0.0
    steps = 0
    foods_eaten = 0

    print(f"\n=== EPISODE {episode + 1}/{num_episodes} ===")

    for step in range(max_steps_per_episode):
        # distance to food BEFORE action
        dist_before = manhattan_distance(state)

        # choose action using epsilon-greedy policy
        action = choose_action(state)

        # take action in environment
        next_state, reward, done = env.step(action)

        # ----- RENDER HERE SO YOU CAN SEE THE SNAKE -----
        env.render()
        print("Action:", action, "Reward:", reward)
        time.sleep(0.2)   # slow it down so you can watch
        # ------------------------------------------------

        # distance to food AFTER action
        dist_after = manhattan_distance(next_state)

        # reward shaping: give small hint
        if not done:  # if we didn't just crash
            if dist_after < dist_before:
                # moved closer to food
                reward += 0.1
            elif dist_after > dist_before:
                # moved farther from food
                reward -= 0.1

        # approximate count: if reward is >= 1, we probably ate food
        if reward >= 1:
            foods_eaten += 1

        steps += 1

        # Q-learning update:
        current_q = Q[(state, action)]
        max_next_q = max(Q[(next_state, a)] for a in ACTIONS)
        td_target = reward + gamma * max_next_q
        td_error = td_target - current_q
        Q[(state, action)] = current_q + alpha * td_error

        state = next_state
        total_reward += reward

        if done:
            print("Episode ended (crash).")
            break

    # after the episode ends, store the results
    rewards_per_episode.append(total_reward)
    foods_per_episode.append(foods_eaten)
    steps_per_episode.append(steps)

    print(f"Episode {episode + 1} finished: total_reward={total_reward:.2f}, "
          f"steps={steps}, foods_eaten={foods_eaten}")

# After training, print averages over all episodes we just ran
avg_reward = sum(rewards_per_episode) / len(rewards_per_episode)
avg_foods = sum(foods_per_episode) / len(foods_per_episode)
avg_steps = sum(steps_per_episode) / len(steps_per_episode)

print("\n=== SUMMARY OVER ALL EPISODES RUN ===")
print(f"Average reward: {avg_reward:.2f}")
print(f"Average foods eaten: {avg_foods:.2f}")
print(f"Average steps survived: {avg_steps:.2f}")
