'''
Change the rectangle's color when we click on the moving rectangle
'''

# Import
import sys
import pygame
import random


# Initialize Pygame
pygame.init()

# Create The Screen
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
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

# Need to set outside the run loop
amt_to_move = 2

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



    # Check If Went Off Edge
    if my_shape_rect.right > screen_width or my_shape_rect.left < 0:
        amt_to_move *= -1

    # Move Rectangles's Position
    my_shape_rect = my_shape_rect.move((amt_to_move, 0))

    # Display It All To The Screen
    screen.fill((100,100,200))
    screen.blit(my_shape, my_shape_rect)
    pygame.display.update()
