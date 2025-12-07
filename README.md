# 🐍 Reinforcement Learning Snake Game
### DSCI 6612 – Artificial Intelligence  
**Instructor:** Dr. Vahid Behzadan  
**Team Members:** Faryal Bahawi, Jatin Nabhoya  

---

## 🔍 Overview
This project implements **Q-learning** in a custom-built Snake environment.  
It includes:

- A **10×10 grid RL environment**
- A **Q-learning agent**
- A **random baseline agent**
- A **trained Q-table (`q_table.pkl`)**
- A **Pygame visual Snake game** (human & AI modes)

The RL environment and the Pygame version are **separate modules**.

---

## 🧱 Environment Description

### State Representation
(snake_x, snake_y, food_x, food_y)
### Actions
UP
DOWN
LEFT
RIGHT

### Reward Function
| Event | Reward |
|-------|--------|
| Eat food | +1 |
| Hit wall | -1 |
| Move toward food | +0.1 |
| Move away from food | -0.1 |
| Normal move | 0 |

---

## 🤖 Q-Learning

### Update Rule
Q(s,a) ← Q(s,a) + α * (reward + γ * max(Q(next_state)) − Q(s,a))

### Hyperparameters
Learning rate α = 0.1
Discount γ = 0.9
Exploration ε = 0.1
Episodes = 5000

The trained Q-table is saved as:
q_table.pkl

---

## 📊 Results

### Random Baseline (200 episodes)
Average reward: -0.83
Foods eaten: 0.17
Survival steps: ~31

### Trained Q-learning Agent (5000 episodes)
Average reward: +0.88
Foods eaten: 0.04
Survival steps: ~12

### Interpretation
- The baseline **wanders randomly** and rarely finds food.  
- The RL agent **moves more intentionally**, demonstrating learning.  
- The snake is 1-block long → low food count is expected.

---

## 🎮 Pygame Game

### Modes
H → Human mode (WASD / Arrow keys)
A → AI mode (simple heuristic, not Q-learning)
SPACE → Start
ESC → Quit

### Sound Effects
eat_drink.wav
game_over.wav

⚠️ *Pygame game is for visualization only; it does NOT use the RL Q-table.*

---

## 📁 Project Structure

```text
RL-Snake-Project/
│
├── snake_env.py           # RL environment
├── q_learning_snake.py    # Q-learning training script (creates q_table.pkl)
├── random_baseline.py     # Random policy agent
├── play_trained_agent.py  # Uses trained Q-table (text playback)
├── play_snake_rl.py       # Older text-mode RL player
├── play_snake_human.py    # Pygame: human mode
├── snake_pygame.py        # Pygame visualization
│
├── q_table.pkl            # Saved Q-table
│
└── sounds/
    ├── eat_drink.wav
    └── game_over.wav
```


# ▶️ How to Run the Project

### 1. Install dependencies
```bash
pip install numpy pygame
```
### 2. Train the RL agent and save Q-table
```bash
python q_learning_snake.py
```
### 3. Run random baseline
```bash
python random_baseline.py
```
### 4. Play using trained Q-table (text mode)
```bash
python play_trained_agent.py
```
### 5. Run Pygame version
```bash
python snake_pygame.py
```

## What We Learned
- How to design a custom RL environment
- How Q-learning improves behavior through trial and error
- How to compare an RL agent with a random baseline
- How to visualize game logic using Pygame
- Why training and visualization must be separate modules


## Future Work
- Connect trained Q-table to Pygame
- Add self-collision and longer snake body
- Replace Q-table with a DQN (Deep Q-Network)
- Improve reward shaping for better food-seeking behavior


## Authors
Faryal Bahawi  
Jatin Nabhoya
