import pygame
pygame.init()
screen = pygame.display.set_mode
((400,500))
bg_image = pygame.transform.scale(pygame.image.load('bg.jpg').convert(),(400,500))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
           
    screen.blit(bg_image,(0,0))
    pygame.display.flip()
pygame.quit()

