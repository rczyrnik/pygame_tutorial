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

''' ADD ME! '''
screen_width=400
screen_height=300

''' CHANGE ME '''
screen = pygame.display.set_mode((screen_width, screen_height))

            # red, green, blue
screen.fill( (100, 100,   200)  )


# ADD A RECTANGLE ---------------------------------

                        # width, height
my_shape = pygame.Surface((100,   50))

              # red, green, blue
my_shape.fill( (0,   0,     255) )

my_shape_rect = my_shape.get_rect()

                        # x, y
my_shape_rect.topleft = (200,150)

# DISPLAY IT ALL ----------------------------------

screen.blit(my_shape, my_shape_rect)

pygame.display.update()


# RUN THE GAME ------------------------------------
''' ADD ME '''
amt_to_move = 2

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
                my_shape.fill((red, green, blue))


    ''' ADD ME! '''
    # Check If Went Off Edge
    if my_shape_rect.right > screen_width or my_shape_rect.left < 0:  # <-- Add me!
        amt_to_move *= -1                                             # <-- Add me!

    # Move Rectangles's Position
    my_shape_rect = my_shape_rect.move((amt_to_move, 0))              # <-- Add me!


    # Display It All To The Screen
    screen.fill((100,100,200))
    screen.blit(my_shape, my_shape_rect)
    pygame.display.update()
