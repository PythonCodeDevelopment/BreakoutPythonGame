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
BLANK_ROWS = 2
WHITE = (255, 255, 255)

#variablize these values if need different size output window
screen = pygame.display.set_mode((600, 800))

screen_rect = screen.get_rect()

#control game speed
#new clock
clock = pygame.time.Clock()

class Brick(pygame.sprite.Sprite):
    def __init__(self, row, col):
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
        
        # position the brick
        
        
        row += BLANK_ROWS  #skill mechanics:add extra blank rows above bricks,this will help to hit more bricks
        self.rect.x = col * brick_width
        self.rect.y = row * brick_height

        



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
bricks = pygame.sprite.Group()

#instantiate ball class
ball = Ball()

paddle = Paddle()

#add ball instance into group to manage things easily
all_sprites.add(ball)

all_sprites.add(paddle)




for row in range(0, NUM_ROWS):
    for col in range(0, BRICKS_PER_ROW):
        brick = Brick(row, col)
        all_sprites.add(brick)
        bricks.add(brick)

score = 0
lives = 3

def draw_text(surface, text, pos=(0, 0), color=WHITE, font_size=20, anchor="topleft"):
    arial = pygame.font.match_font("arial")
    font = pygame.font.Font(arial, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    setattr(text_rect, anchor, pos)
    surface.blit(text_surface, text_rect)
    
    
    
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
        
    #skill mechanics:If the ball hits the left side of the paddle, make the ball go left (negative x speed).
    #Otherwise, make the ball go right (positive x speed).
        
        if ball.rect.centerx < paddle.rect.centerx:
            ball.x_speed = -5
        else:
            ball.x_speed = 5   
        
    # Reset ball if lost
    if ball.lost:
        lives -= 1
        ball.reset()
    
    # Check for ball / brick collision
    collided_brick = pygame.sprite.spritecollideany(ball, bricks)
    if collided_brick:
        score += 1
        collided_brick.kill()
        ball.y_speed *= -1
    
    
    
    #add background color
    screen.fill(BLACK)
    
    all_sprites.draw(screen)
    
    score_text = f"Score: {score} / Lives: {lives}"
    draw_text(screen, score_text, (8, 8))
    
    pygame.display.flip()

pygame.quit()
