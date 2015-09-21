import os
import pygame
from pygame.locals import *

if not pygame.font:
    'Warning, fonts disabled'
if not pygame.mixer:
    'Warning, sounds disabled'

path = '..\data'
pygame.display.set_mode((1600, 800))


class LoadError(Exception):
    pass


def image(name, colorkey):
    fullname = os.path.join(path, name)

    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise LoadError(message)

    image = image.convert()

    if colorkey:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))

        image.set_colorkey(colorkey, RLEACCEL)

    return image


def sound(name):
    class NoneSound(object):
        def play(self):
            pass

    if not pygame.mixer:
        return NoneSound()

    fullname = os.path.join(path, name)

    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', wav
        raise LoadError(message)

    return sound
