import pygame

pygame.init()

keys = pygame.key.get_pressed()
if keys[pygame.K_SPACE]:
    print("Space is pressed")
                                                     