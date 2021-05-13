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

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = screen_rect.center
        self.x_speed = 5
        self.y_speed = 5

    def update(self):
        # Update code goes her

        #bouncing off the side walls
    
        if square.right >= screen_rect.right:
            self.x_speed = -5
        if square.left <= screen_rect.left:
            self.x_speed = 5
        if square.top <= screen_rect.top:
            self.y_speed = 5
        if square.bottom >= screen_rect.bottom:
            self.y_speed = -5
    
        square.x += self.x_speed
        square.y += self.y_speed

#create sprite group
all_sprites = pygame.sprite.Group()

#instantiate ball class
ball = Ball()

#add ball instance into group to manage things easily
all_sprites.add(ball)




running = True

while running:
#animate the square
    
    clock.tick(FPS)
  #1 frame per second
    
    
    
#     Fix the window close-button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            

    
    
    #add background color
    screen.fill(BLACK)
    
    pygame.display.flip()

pygame.quit()
