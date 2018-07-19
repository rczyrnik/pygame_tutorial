'''
Change the rectangle's color when we click anywhere
'''

# IMPORTS
import sys
import pygame
''' ADD ME! '''
import random  # <-- HERE!


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

screen.blit(my_shape, my_shape_rect)

pygame.display.update()


# RUN THE GAME ------------------------------------
''' CHANGE ME! '''
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:  #   <-- ADD ME!

            red = random.randint(0, 255)            #   <-- ADD ME!
            blue = random.randint(0, 255)           #   <-- ADD ME!
            green = random.randint(0, 255)          #   <-- ADD ME!
            my_shape.fill((red, green, blue))       #   <-- ADD ME!

    # Display It All To The Screen              #   <-- ADD ME!
    screen.fill((100,100,200))                  #   <-- ADD ME!
    screen.blit(my_shape, my_shape_rect)        #   <-- ADD ME!
    pygame.display.update()                     #   <-- ADD ME!
