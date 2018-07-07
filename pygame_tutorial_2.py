'''
Change the rectangle's color when we click on the rectangle
'''

# Import
import sys
import pygame
import random

# Initialize Pygame
pygame.init()

# Create The Screen
screen = pygame.display.set_mode((400, 300))
screen.fill((100,100,200))

# Add A Rectangle
rect_color = (0,0,255)
my_shape = pygame.Surface((100,50))
my_shape.fill(rect_color)
my_shape_rect = my_shape.get_rect()    # sort of a description of where the rectangle is on the screen
my_shape_rect.topleft = (200,150)

# Display It All To The Screen
screen.blit(my_shape, my_shape_rect)
pygame.display.update()

# Run The Game
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:

            mouse_position = pygame.mouse.get_pos()

            if my_shape_rect.collidepoint(mouse_position):
                red = random.randint(0, 255)
                blue = random.randint(0, 255)
                green = random.randint(0, 255)
                my_shape.fill((red, blue, green))
                screen.blit(my_shape, my_shape_rect)

    pygame.display.update()
