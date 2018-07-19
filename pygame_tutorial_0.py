'''
Draws a rectangle to the screen
'''

# IMPORTS
import sys
import pygame

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

my_shape_rect = my_shape.get_rect()

                        # x, y
my_shape_rect.topleft = (200,150)


# DISPLAY IT ALL ----------------------------------

            # what? ,   where?
screen.blit(my_shape, my_shape_rect)

pygame.display.update()


# RUN THE GAME ------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
