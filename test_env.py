from snake_env import SnakeEnv

env = SnakeEnv(grid_size=10)

state = env.reset()
print("Initial state:", state)

for step in range(5):
    next_state, reward, done = env.step("UP")
    print(f"Step {step+1}: state={next_state}, reward={reward}, done={done}")
    if done:
        print("Game over.")
        break
