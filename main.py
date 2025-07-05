import pygame, random, os, sys
from pygame.locals import *

pygame.init()

main_directory = os.path.dirname(__file__)
imagens_directory = os.path.join(main_directory, "imagens")

class MyGameText:
    def _init_(self):
        print("Inicializando biblioteca...")
        
    def create_text(self, msg, size, color, font=None):

        if font == None:
            font = "comicsansms"
            
        font = pygame.font.SysFont(font, size, True, False)
        mensagem = f"{msg}"
        text_formatted = font.render(mensagem, False, color)
        return text_formatted
    
mgt = MyGameText()

# Window Variables
height, width = 600, 600
isRunning = True

# Game Variables
fps = 60
points = 0
miss = 0

# Player Variables
x = random.randint(25, 576)
y = 50

vel = 10

# Base Variables
baseX = 100
baseY = 525

icon = pygame.image.load(os.path.join(imagens_directory, 'RainbowBall.png'))

window = pygame.display.set_mode((height, width))
pygame.display.set_caption("Ball Drop")
pygame.display.set_icon(icon)

sky = pygame.image.load(os.path.join(imagens_directory, 'Sky_Background.png'))
sky = pygame.transform.scale(sky, (320*3.2, 256*3))

ball = pygame.image.load(os.path.join(imagens_directory, 'Star.png')).convert_alpha()
ball = pygame.transform.scale(ball, (1024//20, 977//20))

base = pygame.image.load(os.path.join(imagens_directory, 'cloud.png')).convert_alpha()
base = pygame.transform.scale(base, (17*6, 10*3.5))

clock = pygame.time.Clock()

pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

while isRunning:
    clock.tick(fps)
    window.fill((255,255,255))
    os.system('cls')
    text_points = mgt.create_text(f"Points: {points}", 25, (0,0,0))
    text_speed = mgt.create_text(f"Speed: {round(vel)}", 25, (0,0,0))
    text_missed = mgt.create_text(f"Missed: {miss}", 25, (0,0,0))

    ball_rect = ball.get_rect(center=(x, y))
    base_rect = base.get_rect(center=(baseX, baseY))

    y += round(vel)

    if y >= width:
        x = random.randint(25, 576)
        y = 100
        miss += 1

    if ball_rect.colliderect(base_rect):
        x = random.randint(25, 576)
        y = 100
        points += 1
        if vel >= 30:
            vel += 0
        else:
            vel += 0.1
    
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                isRunning = False
                pygame.quit()
                sys.exit()
    
        if event.type == MOUSEMOTION:
            varX, varY = pygame.mouse.get_pos()
            baseX = varX

    window.blit(sky, (-100,0))
    window.blit(text_points, (0,0))
    window.blit(text_speed, (0,25))
    window.blit(text_missed, (0,50))
    window.blit(ball, ball_rect)
    window.blit(base, base_rect)
    pygame.display.flip()

"""
background = https://opengameart.org/users/paur
star = https://opengameart.org/users/galangpiliang
"""