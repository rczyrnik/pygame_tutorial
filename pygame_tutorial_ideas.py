'''
Change the rectangle's color when we click on the moving rectangle
'''

# IMPORTS
import sys
import pygame
import random


# INITIALIZE PYGAME
pygame.init()

# CREATE THE SCREEN -------------------------------
screen_width=800
screen_height=600
screen = pygame.display.set_mode((screen_width, screen_height))
red, blue, green = 100, 100, 200
screen.fill( (red, blue, green)  )

# ADD A RECTANGLE ---------------------------------
my_shape = pygame.image.load('img/more_ideas.png')
my_shape = pygame.transform.smoothscale(my_shape, (screen_width,screen_height))
my_shape_rect = my_shape.get_rect()
my_shape_rect.topleft = (0,0)

# DISPLAY IT ALL ----------------------------------
screen.blit(my_shape, my_shape_rect)
pygame.display.update()

# RUN THE GAME ------------------------------------
amt_to_move = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
