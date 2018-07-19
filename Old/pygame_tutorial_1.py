'''
Change the rectangle's color when we click anywhere
'''

# IMPORTS
import sys
import pygame
import random


# INITIALIZE PYGAME
pygame.init()


# CREATE THE SCREEN -------------------------------

                              # width, height
screen = pygame.display.set_mode((400, 300))

            # red, green, blue
screen.fill( (100, 100,   200)  )


# ADD A RECTANGLE ---------------------------------

                        # width, height
my_shape = pygame.Surface((100,   50))

              # red, green, blue
my_shape.fill( (0,   0,     255) )


# DISPLAY IT ALL ----------------------------------

                  # width, height
screen.blit(my_shape, (200,150))

pygame.display.update()


# RUN THE GAME ------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Color The Rectangle
            red = random.randint(0, 255)
            blue = random.randint(0, 255)
            green = random.randint(0, 255)
            my_shape.fill((red, green, blue))

            # Display It All To The Screen
            screen.blit(my_shape, (200,150))
            pygame.display.update()
