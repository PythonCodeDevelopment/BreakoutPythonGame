import pygame
import random


pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 60  #Frames per second
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BRICKS_PER_ROW = 10
NUM_ROWS = 5



#variablize these values if need different size output window
screen = pygame.display.set_mode((600, 800))

screen_rect = screen.get_rect()

#control game speed
#new clock
clock = pygame.time.Clock()

class Brick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        brick_image = pygame.image.load("brick.png").convert_alpha()
        
        # calculate new size based on BRICKS_PER_ROW
        brick_width = round(screen_rect.width / BRICKS_PER_ROW)
        orig_size = brick_image.get_rect()
        scale_factor = (brick_width / orig_size.width)
        brick_height = round(orig_size.height * scale_factor)
        new_size = (brick_width, brick_height)
        
        
        # scale the image
        self.image = pygame.transform.scale(brick_image, new_size)
        self.rect = self.image.get_rect()

        



class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.reset()
        
    def reset(self):
        self.rect.center = screen_rect.center
        self.x_speed = random.choice((5, -5))
        self.y_speed = 5
        self.lost = False
        
    def update(self):
        # Update code goes her

        #bouncing off the side walls
    
        if self.rect.right >= screen_rect.right:
            self.x_speed = -5
        if self.rect.left <= screen_rect.left:
            self.x_speed = 5
        if self.rect.top <= screen_rect.top:
            self.y_speed = 5
        if self.rect.bottom >= screen_rect.bottom:
            self.lost = True
    
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = screen_rect.center
        #to keep paddle little up from bottom
        self.rect.bottom = screen_rect.bottom - 10
     
    #keyboard controls for paddle
    def update(self):
        #move paddle right or left direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += 10
        if keys[pygame.K_LEFT]:
            self.rect.x -= 10
        
        #keep paddle from going off the screen
        if self.rect.right >= screen_rect.right:
            self.rect.right = screen_rect.right
        if self.rect.left <= screen_rect.left:
            self.rect.left = screen_rect.left
            
            
#create sprite group
all_sprites = pygame.sprite.Group()

#instantiate ball class
ball = Ball()

paddle = Paddle()

#add ball instance into group to manage things easily
all_sprites.add(ball)

all_sprites.add(paddle)

brick = Brick()

all_sprites.add(brick)

running = True

while running:
#animate the square
    
    clock.tick(FPS)
  #1 frame per second
    
    
    
#     Fix the window close-button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
           
    all_sprites.update()
    
    
    # Check for paddle / ball collision
    if pygame.sprite.collide_rect(ball, paddle):
        ball.y_speed = -5
        
    # Reset ball if lost
    if ball.lost:
        ball.reset()
    
    #add background color
    screen.fill(BLACK)
    
    all_sprites.draw(screen)
    
    pygame.display.flip()

pygame.quit()
