import pygame



pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 60  #Frames per second


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
    
    clock.tick(FPS)
  #1 frame per second
    
#     Fix the window close-button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
    #bouncing off the side walls
    
    if square.right >= screen_rect.right:
        x_speed = -5
    if square.left <= screen_rect.left:
        x_speed = 5
    if square.top <= screen_rect.top:
        y_speed = 5
    if square.bottom >= screen_rect.bottom:
        y_speed = -5
    
    
    
    
    
    
    
    
    
    
    square.x += x_speed
    square.y += y_speed
    #add background color
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, square)
    pygame.display.flip()

pygame.quit()
