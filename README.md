# Reinforcement Learning Snake Game  
### Team Members: Faryal Bahawi, Jatin Nabhoya  
### Course: DSCI 6612 – Artificial Intelligence  
### Instructor: Dr. Vahid Behzadan  

---

## 🧠 Project Overview

This project implements a simple but fully custom Reinforcement Learning environment for the classic Snake game. We developed:

- A 10×10 grid Snake environment (built from scratch, no Gym)  
- A Q-learning agent that learns to find food and avoid walls  
- A random baseline agent for comparison  
- A Pygame graphical game with:
  - Human-controlled mode  
  - AI-controlled mode  
  - Sound effects for eating and game over  

The goal of the project was to understand reinforcement learning in a simple environment, compare it to random behavior, and visualize agent performance.

---

## 🎯 Project Objectives

1. Build a custom RL environment for Snake.  
2. Implement and train a Q-learning agent.  
3. Compare the trained agent with a random baseline.  
4. Create a Pygame visual game for human + AI play.  
5. Provide full documentation for reproducibility.

---

## 🧩 Environment Description

The environment uses a 10×10 grid.

### State Representation:
(snake_x, snake_y, food_x, food_y)

### Actions:
- UP  
- DOWN  
- LEFT  
- RIGHT  

### Reward Structure:
| Event | Reward |
|--------|--------|
| Eat food | +1 |
| Hit wall | −1 |
| Move closer to food | +0.1 |
| Move farther from food | −0.1 |
| Normal move | 0 |

---

## 🤖 Q-Learning Algorithm

The agent uses the standard Q-learning update equation:
Q(s,a) = Q(s,a) + α * (reward + γ * max(Q(next_state)) - Q(s,a))


### Hyperparameters:
- Learning rate α = 0.1  
- Discount γ = 0.9  
- Exploration ε = 0.1  
- Episodes = 2000  
- Q-values stored in `defaultdict(float)`  

---

## 📊 Baseline vs Trained Agent Results

### Random Baseline (200 episodes)
- Average reward: −0.83  
- Foods eaten: 0.17  
- Average survival: 30.4 steps  

### Q-Learning Agent (final ~100 episodes)
- Average reward: ~+0.82  
- Foods eaten: ~1.27  
- Average survival: ~11.7 steps  

The Q-learning agent clearly learned to move toward food effectively.

---

## 🎮 Pygame Graphical Game

We added a graphical interface using pygame.

### Human Mode
Arrow keys or WASD to move.  
Snake dies if it hits a wall.

### AI Mode
Loads the saved Q-table and plays automatically.

### Sound Effects
- eat_drink.wav → when snake eats  
- game_over.wav → when snake dies  

---

## 📁 File Structure

RL-Snake-Project/
│
├── snake_env.py
├── q_learning_snake.py
├── random_baseline.py
├── play_snake_rl.py
├── play_snake_human.py
├── snake_pygame.py
│
├── sounds/
│ ├── eat_drink.wav
│ ├── game_over.wav
│
├── slides/
│ └── proposal.pdf
│
└── README.md

---

## ▶️ How to Run the Project

### Install required libraries:
pip install numpy pygame

### Train the agent:
python q_learning_snake.py

### Run baseline:
python random_baseline.py

### Watch RL agent in text mode:
python play_snake_rl.py


### Play text-mode Snake (human):
python play_snake_human.py

### Run the graphical Snake game:
python snake_pygame.py

Controls inside Pygame:
- SPACE → Start  
- H → Human mode  
- A → AI mode  
- ESC → Quit  

---

## 🧪 Evaluation Methodology

We evaluate the agent using:

- Average reward  
- Foods eaten  
- Survival time  
- Visual behavior in Pygame  
- Comparison to random baseline  

These metrics demonstrate whether learning occurred.

---

## 📦 Final Deliverables

- All Python source files  
- RL environment  
- Pygame game with sound  
- Baseline comparison  
- Proposal slides  
- README documentation  
- YouTube demo link  

---

## 🎥 YouTube Demo Video

**Link:** *[Insert unlisted video link here]*

---

## 🏁 Conclusion

This project demonstrates how reinforcement learning can be applied to Snake using Q-learning. The trained agent shows significantly better behavior than a random agent and successfully navigates toward food. The Pygame interface provides a visual and interactive way to observe both human and AI gameplay.

---

## 👩‍💻👨‍💻 Authors  
**Faryal Bahawi**  
**Jatin Nabhoya**
