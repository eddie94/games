import pygame
import sys

pygame.init()
pygame.font.init()

size = width, height = 1280,720
white = 255,255,255
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('Arial',40)

def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()