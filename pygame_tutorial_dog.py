'''
Change the rectangle's color when we click on the rectangle
'''

# Import
import sys
import pygame
import random

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Pet The Dog!")
pygame.mouse.set_visible(0)

pygame.font.init()
myfont = pygame.font.SysFont('Times', 30)

# Create The Screen
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
red, blue, green = 100, 100, 200
screen.fill((red, blue, green ))

# Add A Picture
dog_surface = pygame.image.load('img/white_dog.png')
dog_surface = pygame.transform.scale(dog_surface, (80,60))
dog_surface_rect = dog_surface.get_rect()    # sort of a description of where the rectangle is on the screen
dog_surface_rect.topleft = (200,150)

# Add A Hand
hand_surface = pygame.image.load('img/hand.png')
hand_surface = pygame.transform.scale(hand_surface, (60,60))
hand_surface_rect = hand_surface.get_rect()    # sort of a description of where the rectangle is on the screen
hand_surface_rect.topleft = (200,150)

# Add Text
text_surface = myfont.render('Let\s pet some dog!', False, (0, 0, 0))

# Display It All To The Screen

screen.blit(hand_surface, hand_surface_rect)
screen.blit(dog_surface, dog_surface_rect)
screen.blit(text_surface,(0,0))
pygame.display.update()

# Need to set outside the run loop
amt_to_move_x = amt_to_move_y = 2

# To Determine Pet Ratio
pet_attempts = 0
successful_pets = 0

# Run The Game
while True:
    mouse_position = pygame.mouse.get_pos()
    hand_surface_rect.center = mouse_position

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            pet_attempts += 1
            mouse_position = pygame.mouse.get_pos()

            if dog_surface_rect.collidepoint(mouse_position):
                successful_pets += 1
                red = random.randint(0, 255)
                blue = random.randint(0, 255)
                green = random.randint(0, 255)

            text_surface = myfont.render('Pet Percentage: {}'.format(100*successful_pets//pet_attempts), False, (0, 0, 0))


    # Check If Went Off Edge
    if dog_surface_rect.right > screen_width or dog_surface_rect.left < 0:
        amt_to_move_x *= -1
    if dog_surface_rect.bottom > screen_height or dog_surface_rect.top < 0:
        amt_to_move_y *= -1

    # Move Rectangles's Position
    dog_surface_rect = dog_surface_rect.move((amt_to_move_x, amt_to_move_y))

    # Display It All To The Screen
    screen.fill((red,blue,green))
    screen.blit(dog_surface, dog_surface_rect)
    screen.blit(hand_surface, hand_surface_rect)
    screen.blit(text_surface,(0,0))
    pygame.display.update()
