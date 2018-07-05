'''
Change the rectangle's color when we click on the rectangle

may have to run with pythonw, not python
'''

# Import
import sys
import pygame
import random

# Initialize Pygame
pygame.init()
pygame.mouse.set_visible(0)

# Create The Screen
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
red, blue, green = 100, 100, 200
screen.fill((red, blue, green ))

# Add A Picture
my_shape = pygame.image.load('img/white_dog.png')
my_shape = pygame.transform.scale(my_shape, (80,60))
my_shape_rect = my_shape.get_rect()    # sort of a description of where the rectangle is on the screen
my_shape_rect.topleft = (200,150)

# Add A Hand
my_hand = pygame.image.load('img/hand.png')
my_hand = pygame.transform.scale(my_hand, (60,60))
my_hand_rect = my_shape.get_rect()    # sort of a description of where the rectangle is on the screen
my_hand_rect.topleft = (200,150)

# Display It All To The Screen
screen.blit(my_hand, my_hand_rect)
screen.blit(my_shape, my_shape_rect)
pygame.display.update()

# Need to set outside the run loop
amt_to_move_x = amt_to_move_y = 2

# Run The Game
while True:
    mouse_position = pygame.mouse.get_pos()
    my_hand_rect.center = mouse_position

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


    # Check If Went Off Edge
    if my_shape_rect.right > screen_width or my_shape_rect.left < 0:
        amt_to_move_x *= -1
    if my_shape_rect.bottom > screen_height or my_shape_rect.top < 0:
        amt_to_move_y *= -1

    # Move Rectangles's Position
    my_shape_rect = my_shape_rect.move((amt_to_move_x, amt_to_move_y))

    # Display It All To The Screen
    screen.fill((red,blue,green))
    screen.blit(my_shape, my_shape_rect)
    screen.blit(my_hand, my_hand_rect)
    pygame.display.update()
