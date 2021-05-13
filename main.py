import pygame



pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)

#variablize these values if need different size output window
screen = pygame.display.set_mode((600, 800))

screen_rect = screen.get_rect()

#control game speed
#new clock
clock = pygame.time.Clock()


square = pygame.rect.Rect(0, 0, 50, 50)

square.center = screen_rect.center

x_speed = 5
y_speed = 5


running = True

while running:
#animate the square
    
    clock.tick(1)
  #1 frame per second
    
    square.x += x_speed
    square.y += y_speed
    #add background color
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, square)
    pygame.display.flip()

pygame.quit()
