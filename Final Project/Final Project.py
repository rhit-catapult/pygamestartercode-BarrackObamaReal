import pygame
import sys
import time
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((1550,800))
    pygame.display.set_caption("Final Project")
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
main()