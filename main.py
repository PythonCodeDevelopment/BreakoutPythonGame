import pygame



pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)

#variablize these values if need different size output window
screen = pygame.display.set_mode((600, 800))

#control game speed
#new clock
clock = pygame.time.Clock()


square = pygame.rect.Rect(0, 0, 50, 50)


running = True

while running:
#animate the square
    
    clock.tick(1)
  #1 frame per second
    square.x += 5
    square.y += 5
    #add background color
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, square)
    pygame.display.flip()

pygame.quit()
