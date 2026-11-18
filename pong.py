import random

import pygame
import sys

 #initialize pygame
pygame.init()

#window settings
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

#colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (10, 255, 100)
BLUE = (0, 0, 255)

#clock fpr fps controll
clock = pygame.time.Clock()

#player rectangle
player = pygame.Rect(100, 100, 30, 30)
speed = 5

# apple
apple = pygame.Rect(100, 100, 30, 30)
apple_width, apple_height = 30, 30
apple_x = random.int(2, WIDTH - apple_width)
apple_y = random.int(2, HEIGHT - apple_height)
apple_points = 1

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #movment keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # Drawing
    screen.fill(GREEN)
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, apple)

    pygame.display.flip()
    clock.tick(60)



    

    
        