import pygame
import entities
import sys
import load
from pygame.locals import *

pygame.init()

# setup initial window
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption('Project: Right Click')
icon = load.image('cursor.bmp', (255, 255, 255))
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# setup background
background = pygame.Surface(screen.get_size())
background.fill((50, 50, 50))
screen.blit(background, (0, 0))

# load game objects
button = entities.TestButton()

# main loop
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()

            if button.rect.collidepoint(pos):
                button.click()
        elif event.type == MOUSEBUTTONUP:
            button.unclick()

    screen.blit(background, button.rect, button.rect)
    button.update()
    screen.blit(button.image, button.rect)

    pygame.display.update()
