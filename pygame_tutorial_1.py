'''
Change the rectangle's color when we click
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
my_rect = pygame.Surface((100,50))
my_rect.fill((0,0,255))

# Display It All To The Screen
screen.blit(my_rect, (200,150))
pygame.display.update()

# Run The Game
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
            my_rect.fill((red, blue, green))

            # Display It All To The Screen
            screen.blit(my_rect, (200,150))
            pygame.display.update()
