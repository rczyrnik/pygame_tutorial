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

screen_width=400
screen_height=300

screen = pygame.display.set_mode((screen_width, screen_height))

''' CHANGE ME '''
red, blue, green = 100, 100, 200
screen.fill( (red, blue, green)  )


# ADD A RECTANGLE ---------------------------------

''' CHANGE ME '''
my_shape = pygame.image.load('img/white_dog.png')      # <-- Change me!
my_shape = pygame.transform.smoothscale(my_shape, (80,60))   # <-- Change me!

my_shape_rect = my_shape.get_rect()

                        # x, y
my_shape_rect.topleft = (200,150)




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

        elif event.type == pygame.MOUSEBUTTONDOWN:

            mouse_position = pygame.mouse.get_pos()

            if my_shape_rect.collidepoint(mouse_position):

                red = random.randint(0, 255)
                blue = random.randint(0, 255)
                green = random.randint(0, 255)

                ''' DELETE_ ME! '''
                # my_shape.fill((red, green, blue))    # <-- Delete me!



    # Check If Went Off Edge
    if my_shape_rect.right > screen_width or my_shape_rect.left < 0:
        amt_to_move *= -1

    # Move Rectangles's Position
    my_shape_rect = my_shape_rect.move((amt_to_move, 0))


    # Display It All To The Screen
    ''' CHANGE ME! '''
    screen.fill((red,blue,green))
    screen.blit(my_shape, my_shape_rect)
    pygame.display.update()
