import pygame
import load
from pygame.locals import *
pygame.init()


class Button(pygame.sprite.Sprite):
    """skeleton class for button handling, create a subclass to load in
    assets under self.disabled, self.pressed, self.unpressed, and
    self.hover. self.rect should be a consistent size"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.clicked = False
        self.enabled = True

    def update(self):
        if not self.clicked and self.enabled:
            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                self.image = self.hover
            else:
                self.image = self.unpressed

        if not self.enabled:
            self.image = self.disabled

    def click(self):
        if self.enabled:
            self.clicked = True
            self.image = self.pressed

    def unclick(self):
        if self.enabled:
            self.clicked = False
            self.image = self.unpressed


class TestButton(Button):

    disabled = load.image("button_disabled-240x60.bmp",
                          (0, 0, 0))
    pressed = load.image("button_pressed_green-240x60.bmp",
                         (0, 0, 0))
    unpressed = load.image("button_unpressed_green-240x60.bmp",
                           (0, 0, 0))
    hover = load.image("button_hovered_green-240x60.bmp",
                       (0, 0, 0))
    rect = pressed.get_rect()
