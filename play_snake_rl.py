import time
from snake_env import SnakeEnv
from q_learning_snake import Q, ACTIONS

env = SnakeEnv(grid_size=10)
state = env.reset()

while True:
    env.render()

    # choose the best learned action (no exploration)
    best_action = max(ACTIONS, key=lambda a: Q[(state, a)])

    print("Action:", best_action)

    state, reward, done = env.step(best_action)

    print("Reward:", reward)
    time.sleep(0.3)  # slow the animation down so you can see it

    if done:
        print("Game Over")
        env.render()
        break
