# run as pythonw test_click.py

import pygame
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Whack The Mole!")
# Create The Screen
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))

#Create The Backgound
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((1,166,17))


# Create And Display The Mole
mole_size = 80
mole = pygame.image.load('img/mole.png')
mole = pygame.transform.scale(mole, (mole_size,mole_size))
mole_rect = mole.get_rect()
mole_rect.topleft = (screen_width-mole_size)/2, (screen_height-mole_size)/2

# Create and Display the Hammer
hammer_size = 80
hammer = pygame.image.load('img/hammer_0.png')
hammer = pygame.transform.scale(hammer, (hammer_size,hammer_size))
hammer_rect = hammer.get_rect()
hammer_rect.topleft = (0, 0)


# Add The Mole To The Screen#Display The Background
screen.blit(background, (0, 0))
screen.blit(mole, mole_rect)
screen.blit(hammer, hammer_rect)

# Display The Screen
pygame.display.flip()

# Main Loop
move_x = move_y = level = 1
going = True
while going:
    mouse_pos = pygame.mouse.get_pos()
    hammer_rect.center = mouse_pos

    for event in pygame.event.get():
        if event.type == QUIT:
            going = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            hammer = pygame.image.load('img/hammer_1.png')
            hammer = pygame.transform.scale(hammer, (hammer_size,hammer_size))

            mouse_position = pygame.mouse.get_pos()

            if mole_rect.collidepoint(mouse_position):
                move_x *= 1.3
                move_y *= 1.3
                level += 1
            else:
                print(level)
                going = False

        elif event.type == pygame.MOUSEBUTTONUP:
            hammer = pygame.image.load('img/hammer_0.png')
            hammer = pygame.transform.scale(hammer, (hammer_size,hammer_size))


    # Move the Mole
    mole_rect = mole_rect.move((move_x, move_y))
    if mole_rect.left < 0 or mole_rect.right > screen_width:
        move_x = -move_x
        mole_rect = mole_rect.move((move_x, move_y))

    if mole_rect.top < 0 or mole_rect.bottom > screen_height:
        move_y = -move_y
        mole_rect = mole_rect.move((move_x, move_y))

    #Draw Everything
    screen.blit(background, (0, 0))
    screen.blit(mole, mole_rect)
    screen.blit(hammer, hammer_rect)
    pygame.display.flip()

# Quit The Game
pygame.quit()
