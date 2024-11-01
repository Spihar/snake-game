import pygame
import time
def play():
    pygame.init()
    pygame.mixer.music.load('sanand.mp3')
    pygame.mixer.music.play(loops=-1)
