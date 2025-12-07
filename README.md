# Reinforcement Learning Snake Game  
### Team Members: Faryal Bahawi, Jatin Nabhoya  
### Course: DSCI 6612 – Artificial Intelligence  
### Instructor: Dr. Vahid Behzadan  

---

## 🧠 Project Overview

This project implements a **Reinforcement Learning (RL) agent** for a simplified version of the Snake game on a 10×10 grid.

The work includes:

- A **custom-built Snake environment** (no Gym)
- A **Q-learning agent** trained from scratch
- A **random baseline agent** for comparison
- A **saved Q-table (`q_table.pkl`)** used for inference
- A **Pygame visualization** of the Snake game (separate from RL)

The main goal is to understand how Q-learning works in practice: defining states, actions, rewards, and training an agent through trial and error.

---

## 🎯 Project Objectives

1. Build a simple grid-based Snake environment.  
2. Implement and train a tabular Q-learning agent.  
3. Compare trained behavior vs. a random baseline.  
4. Create a graphical Snake game using Pygame with human + simple AI play.  
5. Provide clear documentation so others can run and extend the project.

---

## 🧩 Environment Description

The environment is a **10×10 grid** with a single-block snake and one food item.

### State Representation

Each state is represented as:

```text
(snake_x, snake_y, food_x, food_y)
Actions

The agent can choose one of four actions:

UP

DOWN

LEFT

RIGHT

Reward Structure

During training, the reward function is:
| Event                  | Reward |
| ---------------------- | ------ |
| Eat food               | +1     |
| Hit wall (game over)   | −1     |
| Normal move            | 0      |
| Move closer to food    | +0.1   |
| Move farther from food | −0.1   |

Reward shaping (+0.1 / −0.1) is used only during training to guide learning.
When running the trained agent for visualization, we can use just the main game rewards.
Q-Learning Algorithm

The agent uses the standard Q-learning update rule:
Q(s, a) ← Q(s, a) + α * [ reward + γ * max_a' Q(next_state, a') − Q(s, a) ]
Hyperparameters

Learning rate α = 0.1

Discount factor γ = 0.9

Exploration rate ε = 0.1 (ε-greedy)

Number of training episodes = 5000

Q-values stored using defaultdict(float)

After training, the Q-table is saved to disk as:
q_table.pkl
This file contains the learned Q-values for state–action pairs and is later loaded for running the trained agent.
Results: Baseline vs Trained Agent
Random Agent Baseline (200 episodes)
From random_baseline.py:
Average reward:     -0.83
Average foods eaten: 0.17
Average steps survived: 31.05
The random agent wanders around the grid, survives by luck for some steps, and almost never eats food.
Trained Q-Learning Agent (5000 episodes)

From q_learning_snake.py (with reward shaping during training):
Average reward:      0.88
Average foods eaten: 0.04
Average steps survived: 12.32
Q-table saved to q_table.pkl
Interpretation

The average reward improves from negative (random) to positive (trained), which shows that learning happened.

The agent learns to move more purposefully toward the food, thanks to reward shaping.

The environment is small and unforgiving (instant death on walls, random food positions), so behavior is still imperfect and episodes are often short.

This is realistic for tabular Q-learning in a simple grid world.

The focus of the project is understanding RL behavior, not creating a perfect Snake player.
Pygame Visualization (Separate from RL)

In addition to the text-based RL environment, we built a Pygame version of Snake for visualization.

Features

Human Mode – control the snake using arrow keys or WASD.

AI Mode – a simple deterministic / rule-based AI (not the Q-learning agent) to demonstrate automated play.

Sound Effects:

eat_drink.wav when eating food

game_over.wav when the snake dies
Important Note

The Pygame version is separate from the RL environment:

RL training happens in the 10×10 grid environment (snake_env.py).

Pygame uses pixel coordinates and its own game loop.

The Pygame AI is not the Q-learning agent; it is a simple strategy used for visualization.

Future work: map the Q-learning agent’s actions from the grid directly into the Pygame world and let the trained agent control the graphical snake.
RL-Snake-Project/
│
├── snake_env.py             # Custom Snake RL environment
├── q_learning_snake.py      # Q-learning training script (saves q_table.pkl)
├── random_baseline.py       # Random agent baseline evaluation
├── play_snake_rl.py         # Uses q_table.pkl to run trained agent in text mode
├── play_snake_human.py      # Human-controlled text-mode Snake
├── snake_pygame.py          # Pygame visualization (human + simple AI)
│
├── q_table.pkl              # Saved trained Q-table (created after training)
├── play_trained_agent.py
│
├── sounds/
│   ├── eat_drink.wav
│   └── game_over.wav
│
├── slides/
│   └── proposal.pdf         # Project proposal slides
│
└── README.md                # This file
How to Run the Project
1. Install dependencies

Make sure you are in your virtual environment (if using one), then run:
pip install numpy pygame
2. Run the random baseline agent
python random_baseline.py
This runs 200 episodes of a random policy and prints the average reward, foods eaten, and steps survived.
3. Train the Q-learning agent
python q_learning_snake.py
This script:

Trains the agent for 5000 episodes

Prints summary statistics

Saves the learned Q-table to q_table.pkl
4. Run the trained RL agent (text mode)
python play_snake_rl.py
This script:

Loads q_table.pkl

Creates a new environment

At each step, chooses the best action according to the Q-table

Shows the grid, action taken, and reward

Ends when the snake crashes
5. Human text-mode Snake
python play_snake_human.py
This version allows manual control (W/A/S/D or similar, depending on implementation) in the console, useful for testing the environment logic.
6. Pygame graphical Snake
python snake_pygame.py
Controls inside Pygame:

SPACE → Start game

H → Human mode

A → AI mode (simple built-in AI, not Q-learning)

ESC → Quit

This provides a visual, interactive version of Snake with sound effects.
Evaluation Methodology

We evaluate the agents using:

Average reward across episodes

Average number of foods eaten

Average survival steps

Comparison with the random baseline

Qualitative behavior (Does the agent move toward food? Does it look less random?)

The trained Q-learning agent shows higher reward and more meaningful behavior compared to the random baseline, even though performance is not perfect.
YouTube Demo Video

Link: [Insert your unlisted YouTube demo link here]

The video walks through:

The environment design

Baseline vs trained results

A short demo of the trained agent in text mode

The Pygame visualization (human + AI mode)
Conclusion

This project demonstrates a full RL pipeline on a classic game:

Designing a custom environment

Implementing Q-learning from scratch

Training and evaluating an agent

Comparing with a random baseline

Building a Pygame visualization for intuitive understanding

The agent successfully learns to improve its reward compared to random behavior.
While it does not perfectly master Snake (which would require more complex methods like Deep Q-Networks and richer state representation), it provides a solid, educational example of tabular Q-learning in action.
Authors

Faryal Bahawi
Jatin Nabhoya
