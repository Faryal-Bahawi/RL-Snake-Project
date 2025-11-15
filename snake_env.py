import random


class SnakeEnv:
    def __init__(self, grid_size=10):
        self.grid_size = grid_size
        self.reset()

    def reset(self):
        """Start a new episode: place snake in the middle, spawn food."""
        x = self.grid_size // 2
        y = self.grid_size // 2
        self.snake = [(x, y)]         
        self.direction = "UP"
        self.done = False

        self._spawn_food()
        return self.get_state()

    def _spawn_food(self):
        """Place food at a random empty cell (not on the snake)."""
        while True:
            fx = random.randint(0, self.grid_size - 1)
            fy = random.randint(0, self.grid_size - 1)
            if (fx, fy) not in self.snake:
                self.food = (fx, fy)
                break

    def get_state(self):
        """Return state = (head_x, head_y, food_x, food_y)."""
        head_x, head_y = self.snake[0]
        food_x, food_y = self.food
        return (head_x, head_y, food_x, food_y)

    def step(self, action):
        """
        Take one step in the environment.

        action: "UP", "DOWN", "LEFT", or "RIGHT"

        returns: (next_state, reward, done)
        """
        if self.done:
            raise ValueError("Game is over. Call reset() before step().")

        head_x, head_y = self.snake[0]
        if action == "UP":
            new_head = (head_x, head_y - 1)
        elif action == "DOWN":
            new_head = (head_x, head_y + 1)
        elif action == "LEFT":
            new_head = (head_x - 1, head_y)
        elif action == "RIGHT":
            new_head = (head_x + 1, head_y)
        else:
            raise ValueError(f"Unknown action: {action}")

        x, y = new_head
        if x < 0 or x >= self.grid_size or y < 0 or y >= self.grid_size:
            self.done = True
            reward = -1
            return self.get_state(), reward, self.done
        if new_head in self.snake:
            self.done = True
            reward = -1
            return self.get_state(), reward, self.done
        self.snake.insert(0, new_head)   
        if new_head == self.food:
            reward = 1          
            self._spawn_food()   
        else:
            reward = 0
            self.snake.pop()  

        next_state = self.get_state()
        self.done = False
        return next_state, reward, self.done
    def render(self):
        grid = [["." for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        # snake head is first element of the snake list
        sx, sy = self.snake[0]
        grid[sy][sx] = "S"

        # food coordinates
        fx, fy = self.food
        grid[fy][fx] = "F"

        # print the grid to terminal
        print("\n".join(" ".join(row) for row in grid))
        print("-" * 20)




