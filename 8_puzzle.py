"""
Make sure to have the dependecies below:
    - pygame

To create an Virtual Environment and isolate the package from your main PIP, do:
    1. Open your terminal at the `8_puzzle.py` directory
    2. Run: python -m venv .venv / python.exe -m venv .venv
    3.
        Linux - source .../8_puzzle_dir/.venv/bin/activate
        Windows - .\Scripts\activate (at the directory where your virtual environment is located)
    4. run `pip install pygame`
    5. Voilà
"""

import pygame
import sys
from random import shuffle

# AI solver with node visualizer
# https://deniz.co/8-puzzle-solver/

class Puzzle8:
    def __init__(self):
        initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        shuffle(initial_state)
        self.state = initial_state
        self.width = 3
        self.tile_size = 60
        self.margin = 6
        self.grid_width = self.width * (self.tile_size + self.margin) - self.margin
        self.grid_height = self.width * (self.tile_size + self.margin) - self.margin
        self.x_offset = (300 - self.grid_width) // 2
        self.y_offset = (300 - self.grid_height) // 2

    def move(self, event):
        zero_position = self.state.index(0)
        if event.key == pygame.K_UP and zero_position > 2:
            self.state[zero_position], self.state[zero_position - 3] = self.state[zero_position - 3], self.state[zero_position]
        elif event.key == pygame.K_DOWN and zero_position < 6:
            self.state[zero_position], self.state[zero_position + 3] = self.state[zero_position + 3], self.state[zero_position]
        elif event.key == pygame.K_LEFT and zero_position % self.width != 0:
            self.state[zero_position], self.state[zero_position - 1] = self.state[zero_position - 1], self.state[zero_position]
        elif event.key == pygame.K_RIGHT and (zero_position + 1) % self.width != 0:
            self.state[zero_position], self.state[zero_position + 1] = self.state[zero_position + 1], self.state[zero_position]

    def draw(self, screen):
        for i, number in enumerate(self.state):
            row = i // self.width
            col = i % self.width
            x = col * (self.tile_size + self.margin) + self.x_offset
            y = row * (self.tile_size + self.margin) + self.y_offset
            if number != 0:
                pygame.draw.rect(screen, (255, 255, 255), (x, y, self.tile_size, self.tile_size))
                font = pygame.font.Font(None, 30)  # Reduced font size
                text_surface = font.render(str(number), True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(x + self.tile_size // 2, y + self.tile_size // 2))
                screen.blit(text_surface, text_rect)
            else:
                pygame.draw.rect(screen, (0, 0, 0), (x, y, self.tile_size, self.tile_size))

    def is_solved(self):
        return self.state == [0, 1, 2, 3, 4, 5, 6, 7, 8]

def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("8Puzzle Game")

    puzzle = Puzzle8()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                puzzle.move(event)
                if puzzle.is_solved():  # Check if the puzzle is solved
                    pygame.quit()
                    sys.exit()

        screen.fill((0, 0, 0))
        puzzle.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
