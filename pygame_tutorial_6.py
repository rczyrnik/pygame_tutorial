# run as pythonw test_click.py

import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Create The Screen
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))


# Create And Display The Mole
mole_size = 80
mole = pygame.image.load('img/mole.png')
mole = pygame.transform.scale(mole, (mole_size,mole_size))
mole_rect = mole.get_rect()
mole_rect.topleft = (screen_width-mole_size)/2, (screen_height-mole_size)/2

# Add The Mole To The Screen
screen.blit(mole, mole_rect)

# Display The Screen
pygame.display.flip()

# Main Loop
going = True
while going:

    for event in pygame.event.get():
        if event.type == QUIT:
            going = False

# Quit The Game
pygame.quit()
