import pygame
import numpy as np
import random
import math
import time
from collections import namedtuple
import atexit
import json
import uuid

def save_logs():
    data = {str(uuid.uuid4()): logs}
    with open('statistics.json', 'a') as file:
        json.dump(data, file)
        file.write('\n')

atexit.register(save_logs)

# Initialize pygame
pygame.init()
pygame.mouse.set_visible(False)
# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Skeet Shooting Simulator")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the target
target_radius = 15
target_speed = .5
targets = []

# Set up the score
score = 0
font = pygame.font.Font(None, 36)

# Set up shooting variables
bullets = 2
reload_time = 2
reloading = False

# Define a named tuple for logs
LogEntry = namedtuple('LogEntry', ['mouse_position_x', 'mouse_position_y', 'mouse_click', 'timestamp', 'score', 'bullets'])
logs = []
last_timestamp = time.time()

# Function to create a new pair of targets
class Target(pygame.Rect):
    def __init__(self):
        self.direction = np.random.choice([-1, 1])
        super().__init__([0, window_width - target_radius * 2, 0][self.direction],
                         window_height - target_radius - 20,
                         target_radius * 2,
                         target_radius * 2)
        speed = target_speed + np.random.random_sample()*.25
        alpha = math.radians(np.random.randint(45,65))
        self.speed_x = speed * math.cos(alpha)
        self.speed_y = speed * math.sin(alpha)
        self.x_ = self.x
        self.y_ = self.y

    def move(self):
        self.x_ -= self.speed_x * self.direction
        self.y_ -= self.speed_y
        self.speed_y -= 0.0005
        self.x = self.x_
        self.y = self.y_

def create_targets():
    target = Target()
    targets.append(target)


# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            logs.append(LogEntry(*event.pos, event.button, time.time(), score, bullets))
            if event.button == 1 and not reloading:
                for target in targets:
                    if target.collidepoint(event.pos):
                        targets.remove(target)
                        score += 1
                        break
                bullets -= 1
                if bullets <= 0:
                    reloading = True

            elif event.button == 3:
                bullets = 2
                reloading = False

    current_timestamp = time.time()
    if current_timestamp - last_timestamp > 0.05:
        logs.append(LogEntry(*pygame.mouse.get_pos(), 0, current_timestamp, score, bullets))
        last_timestamp = current_timestamp

    # Move the targets
    for target in targets:
        target.move()
        if (target.y < -target_radius * 2 or
            target.x < -target_radius * 2 or
            target.x > window_width + target_radius * 2):

            targets.remove(target)

    # Create new targets
    if len(targets) < 2:
        create_targets()

    # Update the display
    window.fill(black)
    for target in targets:
        pygame.draw.circle(window, white, (target.x + target_radius, target.y + target_radius), target_radius)
    score_text = font.render("Score: " + str(score), True, white)
    window.blit(score_text, (10, 10))
    shots_fired_text = font.render("Bullets: " + str(bullets), True, white)
    window.blit(shots_fired_text, (10, 50))

    # Draw crosshair
    crosshair_size = 20
    crosshair_color = (255, 0, 0)
    mouse_pos = pygame.mouse.get_pos()
    crosshair_x = mouse_pos[0] - crosshair_size // 2
    crosshair_y = mouse_pos[1] - crosshair_size // 2
    crosshair = pygame.Rect(crosshair_x, crosshair_y, crosshair_size, crosshair_size)


    # Draw crosshair lines
    pygame.draw.line(window, crosshair_color, (crosshair_x + crosshair_size // 2, crosshair_y),
                     (crosshair_x + crosshair_size // 2, crosshair_y + crosshair_size))
    pygame.draw.line(window, crosshair_color, (crosshair_x, crosshair_y + crosshair_size // 2),
                     (crosshair_x + crosshair_size, crosshair_y + crosshair_size // 2))

    pygame.display.update()


# Quit the game
pygame.quit()