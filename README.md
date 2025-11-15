# Snake Game Reinforcement Learning Project

This project is for my Artificial Intelligence class. I decided to work on a simple version of the Snake game and train an agent using Q-learning. The idea is to get the snake to move around a 10x10 grid, find food, and avoid crashing into the walls.

Everything is written in Python, and I built the environment myself (no gym or external RL libraries). The point was mainly to understand how reinforcement learning works in a small, controlled setting.

---

## 1. How the Environment Works

The game runs on a 10x10 grid.  
The snake is only **one block long** (to keep things simple).  
The state is represented as four numbers:

```
(snake_x, snake_y, food_x, food_y)
```

The actions the snake can take are:
- UP  
- DOWN  
- LEFT  
- RIGHT  

### Rewards
I used a very simple reward system:
- **+1** if the snake eats food  
- **-1** if it hits a wall and dies  
- **0** for a normal move  

I also added “reward shaping” because the agent was learning too slowly:
- Moving **closer** to the food: +0.1  
- Moving **farther** from the food: -0.1  

This helped the agent understand where the food is.

---

## 2. Q-Learning

I used the standard Q-learning formula:

```
Q(s,a) = Q(s,a) + α * (reward + γ * max(Q(next_state)) - Q(s,a))
```

### My hyperparameters:
- learning rate α = 0.1  
- discount factor γ = 0.9  
- exploration ε = 0.1  
- episodes = 2000  

I stored Q-values in a Python `defaultdict(float)` so that every new (state, action) pair starts at 0 automatically.

---

## 3. Baseline vs. Trained Agent

Before training the Q-learning agent, I made a random baseline agent that just picks random moves.  
Here is what happened over 200 random episodes:

- **average reward:** -0.83  
- **foods eaten:** 0.17  
- **average steps alive:** 30.4  

The random snake basically wanders and eventually dies. It almost never finds food.

### After training the Q-learning agent:
(Last ~100 episodes)

- **average reward:** around +0.82  
- **foods eaten:** about 1.27 per episode  
- **average steps:** ~11.7  

So even though the RL snake doesn’t always survive long, it actually **goes for the food**, which is the main goal.  
It learns a strategy, unlike the random one.

---

## 4. How to Run the Code

### Train the agent:
```
python3 q_learning_snake.py
```

### Watch the trained agent play:
```
python3 play_snake_rl.py
```

### Play the game yourself:
```
python3 play_snake_human.py
```

### Run the random baseline:
```
python3 random_baseline.py
```

I only used `numpy` and basic Python libraries.

---

## 5. Files
- `snake_env.py` – the environment  
- `q_learning_snake.py` – training script  
- `play_snake_rl.py` – shows the RL agent moving  
- `play_snake_human.py` – lets me control the snake  
- `random_baseline.py` – random policy for comparison  
- `README.md` – this explanation  

---

## 6. Things I Might Add Later

Not part of the class project, but ideas I might try:
- make the snake grow like the real game  
- add a neural network (DQN)  
- add a graphical interface with pygame  
- plot graphs for rewards and foods eaten  

---

## 7. Quick Conclusion

This project helped me understand Q-learning better.  
The results clearly showed the difference between random behavior and a trained RL agent.  
Even in a small grid, the agent was able to learn how to move toward the food and get rewarded for good decisions.

