import pygame 
import random

pygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1

BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# Background colors

BLUE = pygame.Color('blue')

LIGHTBLUE = pygame.Color('lightblue')

DARKBLUE = pygame.Color('darkblue')

# Sprite colors

YELLOW = pygame.Color('yellow')

MAGENTA = pygame.Color('magenta')

ORANGE = pygame.Color('orange')

WHITE = pygame.Color('white')

class sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]),random.choice([-1, 1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundery_hit = False
        if self.rect.left <= 0 or self.rect.right >=500:
            self.velocity[0] = - self.velocity[0]
            boundery_hit = True
        
        if self.rect.top <= 0 or self.rect.bottom >=500:
           self.velocity[1] = - self.velocity[1]
           boundery_hit = True
        if boundery_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT)) 
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))
def change_background_color():
    global bg_color
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])
         
    
SCREEN_WIDTH,   SCREEN_HEIGHT =500, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("sprite collision")
all_sprites = pygame.sprite.Group()
sprite1 = sprite(pygame.color('black'),20, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(0,SCREEN_WIDTH - sprite1.rect.width),random.randint(0,SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)
sprite2 = sprite(pygame.color('red'),20, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(0,SCREEN_WIDTH - sprite2.rect.width),random.randint(0,SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2) 

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:   sprite1.change_color()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()
    all_sprites.update()    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: sprite2.x -= 3
    if pressed[pygame.K_RIGHT]: sprite2.x+= 3
    if pressed[pygame.K_UP]: sprite2.y -= 3
    if pressed[pygame.K_DOWN]: sprite2.y += 3

    if sprite1.rect.colliderect(sprite2.rect):
        all_sprites.remove(sprite2)
    screen.fill(bg_color)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(240)
    
  
        

    
    
