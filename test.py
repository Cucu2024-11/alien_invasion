import pygame
import sys


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((300, 200))
    pygame.display.set_caption('Test')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)


run_game()
