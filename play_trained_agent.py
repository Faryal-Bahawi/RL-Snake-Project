import time
import pickle
from snake_env import SnakeEnv

# Load trained Q-table
with open("q_table.pkl", "rb") as f:
    Q = pickle.load(f)

ACTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]

env = SnakeEnv(grid_size=10)
state = env.reset()

while True:
    env.render()

    # Choose the best action according to the Q-table
    best_action = max(ACTIONS, key=lambda a: Q.get((state, a), 0))

    print("Action:", best_action)

    next_state, reward, done = env.step(best_action)
    print("Reward:", reward)

    state = next_state
    time.sleep(0.2)

    if done:
        print("Game Over")
        env.render()
        break
