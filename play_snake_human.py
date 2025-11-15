from snake_env import SnakeEnv

env = SnakeEnv(grid_size=10)

state = env.reset()

while True:
    env.render()  # show the board

    action = input("Action (w=UP, s=DOWN, a=LEFT, d=RIGHT, q=quit): ")

    if action == "q":
        break

    if action == "w":
        action = "UP"
    elif action == "s":
        action = "DOWN"
    elif action == "a":
        action = "LEFT"
    elif action == "d":
        action = "RIGHT"
    else:
        print("Invalid key!")
        continue

    state, reward, done = env.step(action)

    print("Reward:", reward)

    if done:
        print("Game over!")
        env.render()
        break
